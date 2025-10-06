# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

import os
import subprocess
import sys
import time
from multiprocessing import Pool
from pathlib import Path

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
import requests


def _query_server(prompt: str, max_tokens: int = 5) -> dict:
    response = requests.post("http://localhost:8000/generate",
                             json={
                                 "prompt": prompt,
                                 "max_tokens": max_tokens,
                                 "temperature": 0,
                                 "ignore_eos": True
                             })
    response.raise_for_status()
    return response.json()


def _query_server_long(prompt: str) -> dict:
    return _query_server(prompt, max_tokens=500)


@pytest.fixture
def api_server(distributed_executor_backend: str):
    script_path = Path(__file__).parent.joinpath(
        "api_server_async_engine.py").absolute()
    commands = [
        sys.executable,
        "-u",
        str(script_path),
        "--model",
        "facebook/opt-125m",
        "--host",
        "127.0.0.1",
        "--distributed-executor-backend",
        distributed_executor_backend,
    ]

    # API Server Test Requires V0.
    my_env = os.environ.copy()
    my_env["VLLM_USE_V1"] = "0"
    uvicorn_process = subprocess.Popen(commands, env=my_env)
    yield
    uvicorn_process.terminate()


@pytest.mark.parametrize("distributed_executor_backend", ["mp", "ray"])
def test_api_server(api_server, distributed_executor_backend: str):
    """
    Run the API server and test it.

    We run both the server and requests in separate processes.

    We test that the server can handle incoming requests, including
    multiple requests at the same time, and that it can handle requests
    being cancelled without crashing.
    """
    with Pool(32) as pool:
        # Wait until the server is ready
        prompts = ["warm up"] * 1
        result = None
        while not result:
            try:
                for r in pool.map(_query_server, prompts):
                    result = r
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(1)

        # Actual tests start here
        # Try with 1 prompt
        for result in pool.map(_query_server, prompts):
            assert result

        num_aborted_requests = requests.get(
            "http://localhost:8000/stats").json()["num_aborted_requests"]
        assert num_aborted_requests == 0

        # Try with 100 prompts
        prompts = ["test prompt"] * 100
        for result in pool.map(_query_server, prompts):
            assert result

    with Pool(32) as pool:
        # Cancel requests
        prompts = ["canceled requests"] * 100
        pool.map_async(_query_server_long, prompts)
        time.sleep(0.01)
        pool.terminate()
        pool.join()

        # check cancellation stats
        # give it some times to update the stats
        time.sleep(1)

        num_aborted_requests = requests.get(
            "http://localhost:8000/stats").json()["num_aborted_requests"]
        assert num_aborted_requests > 0

    # check that server still runs after cancellations
    with Pool(32) as pool:
        # Try with 100 prompts
        prompts = ["test prompt after canceled"] * 100
        for result in pool.map(_query_server, prompts):
            assert result