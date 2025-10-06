# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

import pytest
import torch

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



from vllm.engine.async_llm_engine import SamplerOutput
from vllm.engine.output_processor.single_step import CompletionSequenceGroupOutput
from vllm.compilation.decorators import IntermediateTensors
                           SequenceData, SequenceOutput)

from .core.utils import create_dummy_prompt


@pytest.fixture
def sample_outputs():
    return [
        CompletionSequenceGroupOutput(samples=[
            SequenceOutput(parent_seq_id=0, output_token=i, logprobs={})
        ],
                                      prompt_logprobs=None) for i in range(5)
    ]


@pytest.fixture
def sampler_output(sample_outputs):
    return SamplerOutput(outputs=sample_outputs)


def test_sampler_output_initialization(sampler_output, sample_outputs):
    assert len(sampler_output) == len(sample_outputs)
    assert sampler_output.sampled_token_probs is None
    assert sampler_output.sampled_token_ids is None


def test_sampler_output_getitem(sampler_output, sample_outputs):
    assert sampler_output[2] == sample_outputs[2]


def test_sampler_output_setitem(sampler_output):
    new_output = CompletionSequenceGroupOutput(samples=[
        SequenceOutput(parent_seq_id=0, output_token=99, logprobs={})
    ],
                                               prompt_logprobs=None)
    sampler_output[2] = new_output
    assert sampler_output[2] == new_output


def test_sampler_output_len(sampler_output, sample_outputs):
    assert len(sampler_output) == len(sample_outputs)


def test_sampler_output_eq(sample_outputs):
    sampler_output1 = SamplerOutput(outputs=sample_outputs)
    sampler_output2 = SamplerOutput(outputs=sample_outputs.copy())
    sampler_output3 = SamplerOutput(outputs=sample_outputs[:-1])
    assert sampler_output1 == sampler_output2
    assert sampler_output1 != sampler_output3


def test_sequence_data_prefill():
    seq_data = SequenceData.from_seqs([1, 2, 3, 4])
    assert seq_data.get_num_uncomputed_tokens() == 4
    assert seq_data.get_num_computed_tokens() == 0
    # advance by 2
    seq_data.update_num_computed_tokens(2)
    assert seq_data.get_num_uncomputed_tokens() == 2
    assert seq_data.get_num_computed_tokens() == 2

    # advance by 1
    seq_data.update_num_computed_tokens(1)
    assert seq_data.get_num_uncomputed_tokens() == 1
    assert seq_data.get_num_computed_tokens() == 3

    # append tokens and reset, simulating recompute
    seq_data.append_token_id(1, logprob=0.0)
    seq_data.reset_state_for_recompute()
    assert seq_data.get_num_uncomputed_tokens() == 5
    assert seq_data.get_num_computed_tokens() == 0


def test_sequence_group_stage():
    _, seq_group = create_dummy_prompt("1", 12)
    assert seq_group.is_prefill() is True
    seq_group.update_num_computed_tokens(6)
    assert seq_group.is_prefill() is True
    seq_group.update_num_computed_tokens(5)
    assert seq_group.is_prefill() is True
    seq_group.update_num_computed_tokens(1)
    assert seq_group.is_prefill() is False
    seqs = seq_group.get_seqs()
    assert len(seqs) == 1
    seqs[0].data.append_token_id(1, logprob=0.0)
    for seq in seq_group.get_seqs():
        seq.reset_state_for_recompute()
    assert seq_group.is_prefill() is True
    seq_group.update_num_computed_tokens(5)
    assert seq_group.is_prefill() is True
    seq_group.update_num_computed_tokens(7)
    assert seq_group.is_prefill() is True
    seq_group.update_num_computed_tokens(1)
    assert seq_group.is_prefill() is False


def test_sequence_intermediate_tensors_equal():

    class AnotherIntermediateTensors(IntermediateTensors):
        pass

    intermediate_tensors = IntermediateTensors({})
    another_intermediate_tensors = AnotherIntermediateTensors({})
    assert intermediate_tensors != another_intermediate_tensors

    empty_intermediate_tensors_1 = IntermediateTensors({})
    empty_intermediate_tensors_2 = IntermediateTensors({})
    assert empty_intermediate_tensors_1 == empty_intermediate_tensors_2

    different_key_intermediate_tensors_1 = IntermediateTensors(
        {"1": torch.zeros([2, 4], dtype=torch.int32)})
    difference_key_intermediate_tensors_2 = IntermediateTensors(
        {"2": torch.zeros([2, 4], dtype=torch.int32)})
    assert (different_key_intermediate_tensors_1
            != difference_key_intermediate_tensors_2)

    same_key_different_value_intermediate_tensors_1 = IntermediateTensors(
        {"1": torch.zeros([2, 4], dtype=torch.int32)})
    same_key_different_value_intermediate_tensors_2 = IntermediateTensors(
        {"1": torch.zeros([2, 5], dtype=torch.int32)})
    assert (same_key_different_value_intermediate_tensors_1
            != same_key_different_value_intermediate_tensors_2)

    same_key_same_value_intermediate_tensors_1 = IntermediateTensors(
        {"1": torch.zeros([2, 4], dtype=torch.int32)})
    same_key_same_value_intermediate_tensors_2 = IntermediateTensors(
        {"1": torch.zeros([2, 4], dtype=torch.int32)})
    assert (same_key_same_value_intermediate_tensors_1 ==
            same_key_same_value_intermediate_tensors_2)