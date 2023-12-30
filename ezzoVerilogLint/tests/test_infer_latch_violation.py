"""
This module tests case_violations module functions on multiple verilog_samples
"""

import sys
import os

import pytest

sys.path.append(os.path.realpath(f"{os.path.dirname(__file__)}/.."))
from infer_latch_violation import check_infer_latch
from parse_verilog_fixtures import mini_verilog_sample, verilog_sample


@pytest.fixture
def verilog_snippet():
    return """
    module example;
      reg a, b, c, d, latch;
      always @(a, b, c, d)
      begin
        if (a)
        latch = 1;
        else if(b)
        latch = 0;
        end
    endmodule
    """


def test_uninitreg_on_verilog_code_snippet(verilog_snippet):
    """Test check_infer_latch() on verilog code snippet"""
    violations = check_infer_latch(verilog_snippet)
    assert len(violations) == 1
    assert violations[0] == 8


def test_uninitreg_on_mini_verilog_sample(mini_verilog_sample):
    """Test check_infer_latch() on mini_verilog_sample.v"""
    violations = check_infer_latch(mini_verilog_sample)
    assert len(violations) == 1
    assert violations[0] == 44


def test_uninitreg_on_verilog_sample(verilog_sample):
    """Test check_infer_latch() on verilog_sample.v"""
    violations = check_infer_latch(verilog_sample)
    assert len(violations) == 1
    assert violations[0] == 41
