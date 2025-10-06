# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Test that we handle an Error in model forward and shutdown."""

import asyncio

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

from tests.utils import wait_for_gpu_memory_to_clear
from tests.v1.shutdown.utils import (SHUTDOWN_TEST_THRESHOLD_BYTES,
                                     SHUTDOWN_TEST_TIMEOUT_SEC)
from vllm import LLM, AsyncEngineArgs, SamplingParams
from vllm.distributed import get_tensor_model_parallel_rank
from vllm.model_executor.models.llama import LlamaForCausalLM
from vllm.config.parallel import cuda_device_count_stateless
from vllm.v1.engine.async_llm import AsyncLLM
from vllm.entrypoints.launcher import EngineDeadError

MODELS = ["meta-llama/Llama-3.2-1B"]


def evil_forward(self, *args, **kwargs):
    """Evil forward method that raise an exception after 10 calls."""
    NUMBER_OF_GOOD_PASSES = 10

    if not hasattr(self, "num_calls"):
        self.num_calls = 0

    if (self.num_calls == NUMBER_OF_GOOD_PASSES
            and get_tensor_model_parallel_rank() == 0):
        raise Exception("Simulated illegal memory access on Rank 0!")
    self.num_calls += 1

    return self.model(*args, **kwargs)


@pytest.mark.asyncio
@pytest.mark.parametrize("tensor_parallel_size", [2, 1])
@pytest.mark.parametrize("model", MODELS)
async def test_async_llm_model_error(monkeypatch, tensor_parallel_size: int,
                                     model: str) -> None:
    """Test that AsyncLLM propagates a forward pass error and frees memory.
    
    AsyncLLM always uses an MP client.
    """
    if cuda_device_count_stateless() < tensor_parallel_size:
        pytest.skip(reason="Not enough CUDA devices")

    # Monkeypatch an error in the model.
    monkeypatch.setattr(LlamaForCausalLM, "forward", evil_forward)

    engine_args = AsyncEngineArgs(model=model,
                                  enforce_eager=True,
                                  tensor_parallel_size=tensor_parallel_size)
    async_llm = AsyncLLM.from_engine_args(engine_args)

    async def generate(request_id: str):
        generator = async_llm.generate("Hello my name is",
                                       request_id=request_id,
                                       sampling_params=SamplingParams())
        try:
            async for _ in generator:
                pass
        except Exception as e:
            return e

    NUM_REQS = 3
    tasks = [generate(f"request-{idx}") for idx in range(NUM_REQS)]
    outputs = await asyncio.gather(*tasks)

    # Every request should get an EngineDeadError.
    for output in outputs:
        assert isinstance(output, EngineDeadError)

    # AsyncLLM should be errored.
    assert async_llm.errored

    # We should not be able to make another request.
    with pytest.raises(EngineDeadError):
        async for _ in async_llm.generate("Hello my name is",
                                          request_id="abc",
                                          sampling_params=SamplingParams()):
            raise Exception("We should not get here.")

    # Confirm all the processes are cleaned up.
    wait_for_gpu_memory_to_clear(
        devices=list(range(tensor_parallel_size)),
        threshold_bytes=2 * 2**30,
        timeout_s=60,
    )

    # NOTE: shutdown is handled by the API Server if an exception
    # occurs, so it is expected that we would need to call this.
    async_llm.shutdown()


@pytest.mark.timeout(SHUTDOWN_TEST_TIMEOUT_SEC)
@pytest.mark.parametrize("enable_multiprocessing", [True])
@pytest.mark.parametrize("tensor_parallel_size", [2, 1])
@pytest.mark.parametrize("model", MODELS)
def test_llm_model_error(monkeypatch, tensor_parallel_size: int,
                         enable_multiprocessing: bool, model: str) -> None:
    """Test that LLM propagates a forward pass error and frees memory.
    TODO(andy) - LLM without multiprocessing; LLM with multiprocessing
    and >1 rank
    """
    if cuda_device_count_stateless() < tensor_parallel_size:
        pytest.skip(reason="Not enough CUDA devices")

    with monkeypatch.context() as m:

        MP_VALUE = "1" if enable_multiprocessing else "0"
        m.setenv("VLLM_ENABLE_V1_MULTIPROCESSING", MP_VALUE)

        # Monkeypatch an error in the model.
        m.setattr(LlamaForCausalLM, "forward", evil_forward)

        llm = LLM(model=model,
                  enforce_eager=True,
                  tensor_parallel_size=tensor_parallel_size)

        with pytest.raises(
                EngineDeadError if enable_multiprocessing else Exception):
            llm.generate("Hello my name is Robert and I")

        # Confirm all the processes are cleaned up.
        wait_for_gpu_memory_to_clear(
            devices=list(range(tensor_parallel_size)),
            threshold_bytes=SHUTDOWN_TEST_THRESHOLD_BYTES,
        )