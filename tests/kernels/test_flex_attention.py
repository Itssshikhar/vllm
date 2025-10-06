# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Integration tests for FlexAttention backend vs default backend"""

import random

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



import numpy as np
import pytest
import torch
from packaging import version

from tests.v1.attention.utils import (BatchSpec, create_common_attn_metadata,
                                      create_standard_kv_cache_spec,
                                      create_vllm_config)
from vllm.v1.attention.backends.flex_attention import (
    FlexAttentionMetadataBuilder)

from ..models.utils import check_embeddings_close, check_logprobs_close

TORCH_VERSION = version.parse(torch.__version__)
MINIMUM_TORCH_VERSION = version.parse("2.7.0")
DIRECT_BUILD_VERSION = version.parse("2.9.dev0")


def set_seed(seed):
    """Set seeds for reproducibility"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


@pytest.mark.skipif(
    not torch.cuda.is_available() or TORCH_VERSION < MINIMUM_TORCH_VERSION,
    reason="CUDA not available or PyTorch version < 2.7",
)
def test_flex_attention_vs_default_backend(vllm_runner, monkeypatch):
    """Test that FlexAttention produces the same outputs as the default backend.

    This test compares the outputs from the FlexAttention backend with
    the default backend, ensuring they are similar when using the same seed.
    """
    model_name = "Qwen/Qwen2.5-1.5B-Instruct"
    seed = 42
    max_tokens = 24
    num_logprobs = 5
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
    ]

    # Run with flex attention
    with monkeypatch.context() as m:
        m.setenv("VLLM_USE_V1", "1")
        m.setenv("VLLM_ATTENTION_BACKEND", "FLEX_ATTENTION")

        set_seed(seed)
        with vllm_runner(model_name,
                         runner="generate",
                         tensor_parallel_size=1,
                         num_gpu_blocks_override=128,
                         enforce_eager=True) as llm_flex:
            output_flex = llm_flex.generate_greedy_logprobs(
                prompts, max_tokens, num_logprobs)

    # Run with default backend
    with monkeypatch.context() as m:
        m.setenv("VLLM_USE_V1", "1")
        set_seed(seed)
        with vllm_runner(model_name,
                         runner="generate",
                         tensor_parallel_size=1,
                         num_gpu_blocks_override=128,
                         enforce_eager=True,
                         gpu_memory_utilization=0.85) as llm_default:
            output_default = llm_default.generate_greedy_logprobs(
                prompts, max_tokens, num_logprobs)

    check_logprobs_close(
        outputs_0_lst=output_flex,
        outputs_1_lst=output_default,
        name_0="flex",
        name_1="default",
    )


@pytest.mark.skipif(
    not torch.cuda.is_available() or TORCH_VERSION < MINIMUM_TORCH_VERSION,
    reason="CUDA not available or PyTorch version < 2.7",
)
def test_encoder_flex_attention_vs_default_backend(vllm_runner, monkeypatch):
    """Test that FlexAttention produces the same outputs as the default backend.

    This test compares the outputs from the FlexAttention backend with
    the default backend for encoder models.
    """
    model_name = "BAAI/bge-base-en-v1.5"
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
    ]

    # Run with flex attention
    with monkeypatch.context() as m:
        m.setenv("VLLM_USE_V1", "1")
        m.setenv("VLLM_ATTENTION_BACKEND", "FLEX_ATTENTION")
        with vllm_runner(model_name,
                         runner="pooling",
                         dtype=torch.bfloat16,
                         tensor_parallel_size=1,
                         max_model_len=100,
                         enforce_eager=True) as llm_flex:
            flex_outputs = llm_flex.embed(prompts)

    # Run with default backend
    with monkeypatch.context() as m:
        m.setenv("VLLM_USE_V1", "1")
        with vllm_runner(model_name,
                         runner="pooling",
                         dtype=torch.bfloat16,
                         tensor_parallel_size=1,
                         max_model_len=100,
                         enforce_eager=True) as llm_default:
            default_outputs = llm_default.embed(prompts)

    check_embeddings_close(
        embeddings_0_lst=flex_outputs,
        embeddings_1_lst=default_outputs,
        name_0="flex",
        name_1="default",
        tol=1e-2,
    )


@pytest.mark.skipif(
    not torch.cuda.is_available() or TORCH_VERSION < DIRECT_BUILD_VERSION,
    reason="CUDA not available or PyTorch version < 2.7",
)
def test_block_mask_direct_vs_slow_path():
    """Test that direct path block mask is a superset of slow path.

    The direct path may include extra blocks for performance (over-estimation),
    but must include all blocks that the slow path determines are necessary.
    """
    device = torch.device("cuda")

    vllm_config = create_vllm_config(model_name="meta-llama/Meta-Llama-3-8B",
                                     block_size=16,
                                     max_model_len=1024)
    kv_cache_spec = create_standard_kv_cache_spec(vllm_config)

    # Use a mixed batch that will create groups spanning multiple sequences
    batch_spec = BatchSpec(seq_lens=[35, 64, 128, 256],
                           query_lens=[33, 5, 32, 64],
                           name="test_mixed_batch")

    common_attn_metadata = create_common_attn_metadata(
        batch_spec, vllm_config.cache_config.block_size, device)

    builder = FlexAttentionMetadataBuilder(kv_cache_spec, [], vllm_config,
                                           device)

    metadata_direct = builder.build(common_prefix_len=0,
                                    common_attn_metadata=common_attn_metadata)
    builder.direct_build = False
    metadata_slow = builder.build(common_prefix_len=0,
                                  common_attn_metadata=common_attn_metadata)

    assert metadata_direct.block_mask is not None
    assert metadata_slow.block_mask is not None

    # Extract block indices for comparison, B, H are the same
    direct_indices = metadata_direct.block_mask.kv_indices[0, 0]
    slow_indices = metadata_slow.block_mask.kv_indices[0, 0]
    direct_num = metadata_direct.block_mask.kv_num_blocks[0, 0]
    slow_num = metadata_slow.block_mask.kv_num_blocks[0, 0]

    # main test: every block needed by slow path must be in direct path
    num_groups = direct_num.shape[0]
    all_contained = True
    missing_details = []

    for group_idx in range(num_groups):
        direct_blocks = set(
            direct_indices[group_idx, :direct_num[group_idx]].tolist())
        slow_blocks = set(
            slow_indices[group_idx, :slow_num[group_idx]].tolist())

        missing_blocks = slow_blocks - direct_blocks
        if missing_blocks:
            all_contained = False
            missing_details.append(
                f"Group {group_idx}: missing {sorted(missing_blocks)}")

    assert all_contained, (
        "Direct path is missing blocks required by slow path:\n" +
        "\n".join(missing_details))


if __name__ == "__main__":
    pytest.main([__file__])