# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
from importlib.util import find_spec

import inspect
import logging

# API Probing helpers - auto-generated for compatibility
def safe_create_object(cls, **kwargs):
    """Create object with only valid arguments based on signature."""
    try:
        if not callable(cls):
            raise TypeError(f"{cls} is not callable")
        sig = inspect.signature(cls)
        valid_kwargs = {k: v for k, v in kwargs.items() 
                       if k in sig.parameters and k != "self"}
        return cls(**valid_kwargs)
    except Exception as e:
        logging.warning(f"Failed to create {cls.__name__ if hasattr(cls, '__name__') else cls} with args {list(kwargs.keys())}: {e}")
        raise

def safe_call_function(func, *args, **kwargs):
    """Call function with only valid arguments based on signature."""
    try:
        if not callable(func):
            raise TypeError(f"{func} is not callable")
        sig = inspect.signature(func)
        # Filter kwargs to only valid parameters
        valid_kwargs = {k: v for k, v in kwargs.items() 
                       if k in sig.parameters}
        return func(*args, **valid_kwargs)
    except Exception as e:
        logging.warning(f"Failed to call {func.__name__ if hasattr(func, '__name__') else func} with args {list(kwargs.keys())}: {e}")
        raise

# Specific helpers for common vllm classes
def safe_create_engine_output(**kwargs):
    """Create EngineCoreOutput with compatible arguments."""
    try:
        from vllm.v1.engine import EngineCoreOutput
        return safe_create_object(EngineCoreOutput, **kwargs)
    except ImportError:
        try:
            from vllm.engine import EngineCoreOutput  
            return safe_create_object(EngineCoreOutput, **kwargs)
        except ImportError:
            raise ImportError("EngineCoreOutput not found in vllm")

def safe_create_sampling_params(**kwargs):
    """Create SamplingParams with compatible arguments."""
    try:
        from vllm import SamplingParams
        return safe_create_object(SamplingParams, **kwargs)
    except ImportError:
        try:
            from vllm.sampling_params import SamplingParams
            return safe_create_object(SamplingParams, **kwargs)
        except ImportError:
            raise ImportError("SamplingParams not found in vllm")

def safe_create_llm(**kwargs):
    """Create LLM with compatible arguments."""
    try:
        from vllm import LLM
        return safe_create_object(LLM, **kwargs)
    except ImportError:
        raise ImportError("LLM not found in vllm")



import inspect
import logging

# API Probing helpers - auto-generated for compatibility
def safe_create_object(cls, **kwargs):
    """Create object with only valid arguments based on signature."""
    try:
        if not callable(cls):
            raise TypeError(f"{cls} is not callable")
        sig = inspect.signature(cls)
        valid_kwargs = {k: v for k, v in kwargs.items() 
                       if k in sig.parameters and k != "self"}
        return cls(**valid_kwargs)
    except Exception as e:
        logging.warning(f"Failed to create {cls.__name__ if hasattr(cls, '__name__') else cls} with args {list(kwargs.keys())}: {e}")
        raise

def safe_call_function(func, *args, **kwargs):
    """Call function with only valid arguments based on signature."""
    try:
        if not callable(func):
            raise TypeError(f"{func} is not callable")
        sig = inspect.signature(func)
        # Filter kwargs to only valid parameters
        valid_kwargs = {k: v for k, v in kwargs.items() 
                       if k in sig.parameters}
        return func(*args, **valid_kwargs)
    except Exception as e:
        logging.warning(f"Failed to call {func.__name__ if hasattr(func, '__name__') else func} with args {list(kwargs.keys())}: {e}")
        raise

# Specific helpers for common vllm classes
def safe_create_engine_output(**kwargs):
    """Create EngineCoreOutput with compatible arguments."""
    try:
        from vllm.v1.engine import EngineCoreOutput
        return safe_create_object(EngineCoreOutput, **kwargs)
    except ImportError:
        try:
            from vllm.engine import EngineCoreOutput  
            return safe_create_object(EngineCoreOutput, **kwargs)
        except ImportError:
            raise ImportError("EngineCoreOutput not found in vllm")

def safe_create_sampling_params(**kwargs):
    """Create SamplingParams with compatible arguments."""
    try:
        from vllm import SamplingParams
        return safe_create_object(SamplingParams, **kwargs)
    except ImportError:
        try:
            from vllm import SamplingParams
            return safe_create_object(SamplingParams, **kwargs)
        except ImportError:
            raise ImportError("SamplingParams not found in vllm")

def safe_create_llm(**kwargs):
    """Create LLM with compatible arguments."""
    try:
        from vllm import LLM
        return safe_create_object(LLM, **kwargs)
    except ImportError:
        raise ImportError("LLM not found in vllm")



import inspect
import logging

# API Probing helpers - auto-generated for compatibility
def safe_create_object(cls, **kwargs):
    """Create object with only valid arguments based on signature."""
    try:
        if not callable(cls):
            raise TypeError(f"{cls} is not callable")
        sig = inspect.signature(cls)
        valid_kwargs = {k: v for k, v in kwargs.items() 
                       if k in sig.parameters and k != "self"}
        return cls(**valid_kwargs)
    except Exception as e:
        logging.warning(f"Failed to create {cls.__name__ if hasattr(cls, '__name__') else cls} with args {list(kwargs.keys())}: {e}")
        raise

def safe_call_function(func, *args, **kwargs):
    """Call function with only valid arguments based on signature."""
    try:
        if not callable(func):
            raise TypeError(f"{func} is not callable")
        sig = inspect.signature(func)
        # Filter kwargs to only valid parameters
        valid_kwargs = {k: v for k, v in kwargs.items() 
                       if k in sig.parameters}
        return func(*args, **valid_kwargs)
    except Exception as e:
        logging.warning(f"Failed to call {func.__name__ if hasattr(func, '__name__') else func} with args {list(kwargs.keys())}: {e}")
        raise

# Specific helpers for common vllm classes
def safe_create_engine_output(**kwargs):
    """Create EngineCoreOutput with compatible arguments."""
    try:
        from vllm.v1.engine import EngineCoreOutput
        return safe_create_object(EngineCoreOutput, **kwargs)
    except ImportError:
        try:
            from vllm.engine import EngineCoreOutput  
            return safe_create_object(EngineCoreOutput, **kwargs)
        except ImportError:
            raise ImportError("EngineCoreOutput not found in vllm")

def safe_create_sampling_params(**kwargs):
    """Create SamplingParams with compatible arguments."""
    try:
        from vllm import SamplingParams
        return safe_create_object(SamplingParams, **kwargs)
    except ImportError:
        try:
            from vllm import SamplingParams
            return safe_create_object(SamplingParams, **kwargs)
        except ImportError:
            raise ImportError("SamplingParams not found in vllm")

def safe_create_llm(**kwargs):
    """Create LLM with compatible arguments."""
    try:
        from vllm import LLM
        return safe_create_object(LLM, **kwargs)
    except ImportError:
        raise ImportError("LLM not found in vllm")



import pytest
import torch

import vllm.envs as envs
from vllm.compilation.collective_fusion import AllReduceFusionPass
from vllm.compilation.fix_functionalization import FixFunctionalizationPass
from vllm.compilation.noop_elimination import NoOpEliminationPass
from vllm.config import (CompilationConfig, CompilationLevel, DeviceConfig,
                         ModelConfig, PassConfig, VllmConfig)
from vllm.distributed import tensor_model_parallel_all_reduce
from vllm.distributed.parallel_state import (init_distributed_environment,
                                             initialize_model_parallel)
from vllm.model_executor.layers.layernorm import RMSNorm
from vllm.model_executor.layers.quantization.utils.w8a8_utils import (
    GroupShape, QuantFP8)
from vllm._custom_ops import current_platform
from vllm.utils import update_environment_variables

from ..utils import has_module_attribute, multi_gpu_test
from .backend import TestBackend


class TestAllReduceRMSNormModel(torch.nn.Module):

    def __init__(self, hidden_size=16, token_num=16, eps=1e-6):
        super().__init__()
        self.hidden_size = hidden_size
        self.eps = eps
        self.norm = RMSNorm(hidden_size, eps)

    def forward(self, hidden_states, residual):
        view = hidden_states.reshape(-1, self.hidden_size)
        all_reduce = tensor_model_parallel_all_reduce(view)
        norm = self.norm(all_reduce)
        return norm

    def ops_in_model_before(self):
        return [torch.ops.vllm.all_reduce.default]

    def ops_in_model_after(self):
        return [torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default]


class TestAllReduceFusedAddRMSNormModel(torch.nn.Module):

    def __init__(self, hidden_size=16, token_num=16, eps=1e-6):
        super().__init__()
        self.hidden_size = hidden_size
        self.eps = eps
        self.norm = RMSNorm(hidden_size, eps)

    def forward(self, hidden_states, residual):
        view = hidden_states.reshape(-1, self.hidden_size)
        all_reduce = tensor_model_parallel_all_reduce(view)
        norm, _ = self.norm(all_reduce, residual)
        return norm

    def ops_in_model_before(self):
        return [torch.ops.vllm.all_reduce.default]

    def ops_in_model_after(self):
        return [torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default]


class TestAllReduceFusedAddRMSNormStaticQuantFP8Model(torch.nn.Module):

    def __init__(self, hidden_size=16, token_num=16, eps=1e-6):
        super().__init__()
        self.hidden_size = hidden_size
        self.eps = eps
        self.norm = RMSNorm(hidden_size, eps)
        self.quant_fp8 = QuantFP8(static=True,
                                  group_shape=GroupShape.PER_TENSOR)
        self.scale = torch.rand(1, dtype=torch.float32)
        self.output = torch.empty((token_num, hidden_size),
                                  dtype=torch.float32)

    def forward(self, hidden_states, residual):
        view = hidden_states.reshape(-1, self.hidden_size)
        all_reduce = tensor_model_parallel_all_reduce(view)
        norm_output, residual_output = self.norm(all_reduce, residual)
        torch.ops._C.static_scaled_fp8_quant(self.output,
                                             norm_output.contiguous(),
                                             self.scale)
        return self.output, residual_output

    def ops_in_model_after(self):
        return [torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default]

    def ops_in_model_before(self):
        return [
            torch.ops.vllm.all_reduce.default,
            torch.ops._C.static_scaled_fp8_quant.default
        ]


class TestAllReduceFusedAddRMSNormStaticQuantFP4Model(torch.nn.Module):

    def __init__(self, hidden_size=16, token_num=16, eps=1e-6):
        super().__init__()
        self.hidden_size = hidden_size
        self.eps = eps
        self.norm = RMSNorm(hidden_size, eps)
        self.scale = torch.rand(1, dtype=torch.float32)
        self.output = torch.empty((token_num, hidden_size),
                                  dtype=torch.float32)

        round_up = lambda x, y: (x + y - 1) // y * y
        rounded_m = round_up(token_num, 128)
        scale_n = hidden_size // 16
        rounded_n = round_up(scale_n, 4)
        self.output_scale = torch.empty((rounded_m, rounded_n // 4),
                                        dtype=torch.int32)

    def forward(self, hidden_states, residual):
        view = hidden_states.reshape(-1, self.hidden_size)
        all_reduce = tensor_model_parallel_all_reduce(view)
        norm_output, residual_output = self.norm(all_reduce, residual)
        norm_output = norm_output.reshape(-1, norm_output.shape[-1])
        torch.ops._C.scaled_fp4_quant(self.output, norm_output,
                                      self.output_scale, self.scale)
        return self.output, residual_output, self.output_scale

    def ops_in_model_after(self):
        return [torch.ops.vllm.flashinfer_trtllm_fused_allreduce_norm.default]

    def ops_in_model_before(self):
        return [
            torch.ops.vllm.all_reduce.default,
            torch.ops._C.scaled_fp4_quant.default
        ]


@multi_gpu_test(num_gpus=2)
@pytest.mark.parametrize(
    "test_model",
    [
        TestAllReduceRMSNormModel,
        TestAllReduceFusedAddRMSNormModel,
        TestAllReduceFusedAddRMSNormStaticQuantFP8Model,
        # TODO: Enable with torch==2.8.0
        # TestAllReduceFusedAddRMSNormStaticQuantFP4Model,
    ])
@pytest.mark.parametrize("batch_size", [8])
@pytest.mark.parametrize("seq_len", [8])
@pytest.mark.parametrize("hidden_size", [16])
@pytest.mark.parametrize("dtype", [torch.bfloat16])
@pytest.mark.skipif(envs.VLLM_TARGET_DEVICE not in ["cuda"],
                    reason="Only test on CUDA")
@pytest.mark.skipif(
    not find_spec("flashinfer")
    or not has_module_attribute("flashinfer.comm", "trtllm_allreduce_fusion"),
    reason="flashinfer is not found or flashinfer "
    "is not compiled with trtllm_allreduce_fusion")
def test_all_reduce_fusion_pass_replace(test_model: torch.nn.Module,
                                        batch_size: int, seq_len: int,
                                        hidden_size: int, dtype: torch.dtype):
    num_processes = 2
    if (test_model == TestAllReduceFusedAddRMSNormStaticQuantFP4Model
            and not current_platform.has_device_capability(100)):
        pytest.skip("Skip as nvfp4 is only supported on "
                    "devices with compute capability 10.0 (Blackwell)")

    def run_torch_spawn(fn, nprocs):
        torch.multiprocessing.spawn(fn,
                                    args=(num_processes, test_model,
                                          batch_size, seq_len, hidden_size,
                                          dtype),
                                    nprocs=nprocs)

    run_torch_spawn(all_reduce_fusion_pass_on_test_model, num_processes)


def all_reduce_fusion_pass_on_test_model(local_rank: int, world_size: int,
                                         test_model_cls: torch.nn.Module,
                                         batch_size: int, seq_len: int,
                                         hidden_size: int, dtype: torch.dtype):
    current_platform.seed_everything(0)

    device = torch.device(f"cuda:{local_rank}")
    torch.cuda.set_device(device)
    torch.set_default_device(device)
    torch.set_default_dtype(dtype)

    update_environment_variables({
        'RANK': str(local_rank),
        'LOCAL_RANK': str(local_rank),
        'WORLD_SIZE': str(world_size),
        'MASTER_ADDR': 'localhost',
        'MASTER_PORT': '12345',
    })

    init_distributed_environment()
    initialize_model_parallel(tensor_model_parallel_size=world_size)

    vllm_config = VllmConfig(compilation_config=CompilationConfig(
        level=CompilationLevel.PIECEWISE,
        custom_ops=["+rms_norm", "+quant_fp8"]))
    vllm_config.compilation_config.pass_config = PassConfig(
        enable_fi_allreduce_fusion=True, enable_noop=True)
    vllm_config.device_config = DeviceConfig(device=torch.device("cuda"))

    # this is a fake model name to construct the model config
    # in the vllm_config, it's not really used.
    model_name = "nm-testing/TinyLlama-1.1B-Chat-v1.0-FP8-e2e"
    vllm_config.model_config = ModelConfig(model=model_name,
                                           trust_remote_code=True,
                                           dtype=dtype,
                                           seed=42)

    all_reduce_fusion_pass = AllReduceFusionPass(vllm_config)
    noop_pass = NoOpEliminationPass(vllm_config)
    func_pass = FixFunctionalizationPass(vllm_config)

    backend = TestBackend(all_reduce_fusion_pass, noop_pass, func_pass)

    token_num = batch_size * seq_len
    model = test_model_cls(hidden_size, token_num)

    hidden_states = torch.randn((token_num, hidden_size), requires_grad=False)
    residual = torch.randn((token_num, hidden_size), requires_grad=False)

    compiled_model = torch.compile(model, backend=backend)
    compiled_model(hidden_states, residual)

    backend.check_before_ops(model.ops_in_model_before(), fully_replaced=False)
    backend.check_after_ops(model.ops_in_model_after())
    del all_reduce_fusion_pass