"""
This module tests case_violations module functions on multiple verilog_samples
"""

import sys
import os

import pytest

sys.path.append(os.path.realpath(f"{os.path.dirname(__file__)}/.."))
from case_violations import catch_non_full_case, catch_non_parallel_case
from parse_verilog_fixtures import mini_verilog_sample, verilog_sample


@pytest.fixture
def verilog_snippet():
    return """reg [1:0] result;
    casez (result)
        1 : f = 2'b11;
        0: f=2'b10;
        0: f=2'b10;
        2'b10: f=2'b00;
    endcase
    """


########################## Full Case testing ##########################


def test_fullcase_on_verilog_code_snippet(verilog_snippet):
    """Test catch_non_full_case() on verilog code snippet"""
    line_numbers = catch_non_full_case(verilog_snippet)
    assert len(line_numbers) == 1
    assert line_numbers[0] == 1


def test_fullcase_on_mini_verilog_sample(mini_verilog_sample):
    """Test catch_non_full_case() on mini_verilog_sample.v"""
    line_numbers = catch_non_full_case(mini_verilog_sample)
    assert len(line_numbers) == 2
    assert line_numbers[0] == 7
    assert line_numbers[1] == 32


def test_fullcase_on_verilog_sample(verilog_sample):
    """Test catch_non_full_case() on verilog_sample.v"""
    line_numbers = catch_non_full_case(verilog_sample)
    assert len(line_numbers) == 2
    assert line_numbers[0] == 54
    assert line_numbers[1] == 62


########################## Paralell Case testing ##########################


def test_parallelcase_on_verilog_code_snippet(verilog_snippet):
    """Test catch_non_parallel_case() on verilog code snippet"""
    line_numbers = catch_non_parallel_case(verilog_snippet)
    assert len(line_numbers) == 1
    assert line_numbers[0] == 1


def test_parallelcase_on_mini_verilog_sample(mini_verilog_sample):
    """Test catch_non_parallel_case() on mini_verilog_sample.v"""
    line_numbers = catch_non_parallel_case(mini_verilog_sample)
    assert len(line_numbers) == 1
    assert line_numbers[0] == 32


def test_parallelcase_on_verilog_sample(verilog_sample):
    """Test catch_non_parallel_case() on verilog_sample.v"""
    line_numbers = catch_non_parallel_case(verilog_sample)
    assert len(line_numbers) == 1
    assert line_numbers[0] == 62
