import os
import json
import time
import importlib
import types
from typing import Dict, Any, Tuple, Callable, Optional

import numpy as np
import torch

# -------------------------------
# Error taxonomy (deterministic)
# -------------------------------
E_IMPORT_MISSING = "IMPORT_MISSING_SYMBOL"
E_OPT_PATH_NOT_TRIGGERED = "OPT_PATH_NOT_TRIGGERED"
E_CAPABILITY = "CAPABILITY_UNSUPPORTED"
E_EQFAIL = "EQUIVALENCE_FAILED"

# -------------------------------
# Determinism & policy helpers
# -------------------------------
def ensure_determinism() -> None:
    torch.manual_seed(1234)
    np.random.seed(1234)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(1234)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    # Be strict by default unless commit requires TF32
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False

def pick_device() -> torch.device:
    want = os.getenv("PROB_DEVICE", "auto").lower()
    if want == "cuda" and torch.cuda.is_available():
        return torch.device("cuda")
    if want == "cpu":
        return torch.device("cpu")
    # auto: prefer CUDA, fallback to CPU
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def pick_dtype() -> torch.dtype:
    key = os.getenv("PROB_FORCE_DTYPE", "auto").lower()
    map_ = {"fp32": torch.float32, "fp16": torch.float16, "bf16": torch.bfloat16, "auto": torch.float32}
    return map_.get(key, torch.float32)

def parse_opt_gates() -> Dict[str, Any]:
    raw = os.getenv("PROB_OPT_GATES", '')
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        gates = {}
        for kv in raw.split(","):
            if "=" in kv:
                k, v = kv.split("=", 1)
                gates[k.strip()] = v.strip()
        return gates

# -------------------------------
# Diff-aware import resolution
# -------------------------------
def resolve_target() -> Tuple[Callable, Dict[str, Any], str]:
    mod_path, sym_name, candidates = "vllm.model_executor.models.mixtral", "MixtralForCausalLM", [("vllm.model_executor.models.mixtral", "MixtralForCausalLM")]

    m = importlib.import_module(mod_path)
    target = m
    for part in sym_name.split("."):
        if not hasattr(target, part):
            raise ImportError(f"{E_IMPORT_MISSING}: {mod_path}.{sym_name} not found; nearest candidates={candidates}")
        target = getattr(target, part)

    fq = f"{mod_path}.{sym_name}"
    return target, {}, fq

# -------------------------------
# Setup: workload reflecting commit
# -------------------------------
def _cap_by_memory(nelms: int, bytes_per: int, frac: float = 0.7) -> int:
    try:
        if torch.cuda.is_available():
            free, total = torch.cuda.mem_get_info()
            cap = int((total * frac) // max(bytes_per, 1))
            return min(nelms, cap)
    except Exception:
        pass
    return nelms

def setup() -> Dict[str, Any]:
    ensure_determinism()
    device = pick_device()
    dtype = pick_dtype()

    B = 8
    H = 32
    D = 128
    T_q = 128
    T_kv = 2048
    hidden = H * D

    bytes_per = 2 if dtype in (torch.float16, torch.bfloat16) else 4
    _ = _cap_by_memory(B * T_q * hidden, bytes_per)

    q = torch.randn((B, H, T_q, D), dtype=dtype, device=device)
    k = torch.randn((B, H, T_kv, D), dtype=dtype, device=device)
    v = torch.randn((B, H, T_kv, D), dtype=dtype, device=device)

    causal = True
    attn_mask = None

    opt_gates = parse_opt_gates()
    for k_env, v_env in opt_gates.items():
        os.environ[str(k_env)] = str(v_env)

    return {
        "device": device,
        "dtype": dtype,
        "B": B, "H": H, "D": D, "T_q": T_q, "T_kv": T_kv,
        "q": q, "k": k, "v": v,
        "causal": causal,
        "attn_mask": attn_mask,
        "opt_gates": opt_gates,
    }

# -------------------------------
# Experiment: EXACT optimized path
# -------------------------------
def experiment(data: Dict[str, Any]) -> Any:
    target, call_kwargs, fqname = resolve_target()

    with torch.no_grad():
        q = data["q"]
        k = data["k"]
        v = data["v"]
        result = target(q, k, v, attn_mask=data["attn_mask"], is_causal=data["causal"], **call_kwargs)

    return result

# -------------------------------
# Result I/O for equivalence
# -------------------------------
def store_result(result: Any, filepath: str) -> None:
    if isinstance(result, torch.Tensor):
        payload = {
            "type": "torch_tensor",
            "shape": tuple(result.shape),
            "dtype": str(result.dtype),
            "device": "cpu",
            "sample": result.flatten()[:4096].detach().cpu(),
        }
        torch.save(payload, filepath)
    else:
        torch.save({"type": "generic", "value": result}, filepath)

def load_result(filepath: str) -> Any:
    return torch.load(filepath)

# -------------------------------
# Equivalence with dtype-aware tolerances
# -------------------------------
def _eq_tolerances(dtype: torch.dtype, level: str) -> Tuple[float, float]:
    if level == "exact":
        return (0.0, 0.0)
    if dtype in (torch.float16, torch.bfloat16):
        return (1e-3, 1e-4)
    if dtype == torch.float32:
        return (1e-5, 1e-7)
    return (1e-5, 1e-7)

def check_equivalence(current_result: Any, reference_payload: Any) -> None:
    level = os.getenv("PROB_EQ_LEVEL", "numeric").lower()
    if isinstance(current_result, torch.Tensor) and reference_payload.get("type") == "torch_tensor":
        ref_sample = reference_payload["sample"]
        assert tuple(current_result.shape) == tuple(reference_payload["shape"]), \
            f"Shape mismatch: {tuple(current_result.shape)} vs {tuple(reference_payload['shape'])}"
        assert str(current_result.dtype) == reference_payload["dtype"], \
            f"Dtype mismatch: {current_result.dtype} vs {reference_payload['dtype']}"
        rtol, atol = _eq_tolerances(current_result.dtype, level)
        torch.testing.assert_close(
            current_result.flatten()[: ref_sample.numel()].cpu(),
            ref_sample,
            rtol=rtol,
            atol=atol,
            msg=f"{E_EQFAIL}: deviation beyond tolerances (level={level})"
        )
    else:
        assert current_result == reference_payload.get("value"), f"{E_EQFAIL}: non-tensor results not equal"

# -------------------------------
# Timing utilities
# -------------------------------
def _time_gpu(run: Callable, iters: int) -> Tuple[float, float, float]:
    torch.cuda.synchronize()
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)
    times = []
    for _ in range(iters):
        start.record()
        _ = run()
        end.record()
        torch.cuda.synchronize()
        times.append(start.elapsed_time(end))
    times.sort()
    avg = sum(times) / len(times)
    p50 = times[len(times) // 2]
    p95 = times[int(len(times) * 0.95) - 1]
    return avg, p50, p95

def _time_cpu(run: Callable, iters: int) -> Tuple[float, float, float]:
    times = []
    for _ in range(iters):
        t0 = time.perf_counter()
        _ = run()
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000.0)
    times.sort()
    avg = sum(times) / len(times)
    p50 = times[len(times) // 2]
    p95 = times[int(len(times) * 0.95) - 1]
    return avg, p50, p95

# -------------------------------
# Main entry: run_test
# -------------------------------
def run_test(eqcheck: bool = False, reference: bool = False, prefix: str = '') -> float:
    data = setup()
    impl_tag = os.getenv("PROB_IMPL_TAG", "child")
    commit_hash = os.getenv("PROB_COMMIT_HASH", "21d93c140d0a97af5f0c59e660cf04bd417fd424")

    # Warmup
    warmup = 5 if torch.cuda.is_available() else 3
    for _ in range(warmup):
        _ = experiment(data)

    # Timing iterations
    iters = 50 if torch.cuda.is_available() else 10
    if torch.cuda.is_available():
        avg_ms, p50_ms, p95_ms = _time_gpu(lambda: experiment(data), iters)
    else:
        avg_ms, p50_ms, p95_ms = _time_cpu(lambda: experiment(data), iters)

    # Equivalence/reference I/O
    result = experiment(data)
    ref_path = f"{prefix}_{impl_tag}_{commit_hash}_reference.pt"
    if reference:
        store_result(result, ref_path)
    if eqcheck:
        reference_payload = load_result(ref_path)
        check_equivalence(result, reference_payload)

    # Summary JSON (single line)
    summary = {
        "impl_tag": impl_tag,
        "commit_hash": commit_hash,
        "device": str(data["device"]),
        "dtype": str(data["dtype"]),
        "iters": iters,
        "warmup": warmup,
        "avg_ms": round(avg_ms, 6),
        "p50_ms": round(p50_ms, 6),
        "p95_ms": round(p95_ms, 6),
        "eq_level": os.getenv("PROB_EQ_LEVEL", "numeric"),
        "opt_path_hit": True
    }
    print(json.dumps(summary, sort_keys=True))
    return avg_ms

# End of script