"""
This module tests arithmetic_overflow_violation module functions on multiple verilog_samples
"""

import sys
import os

import pytest

sys.path.append(os.path.realpath(f"{os.path.dirname(__file__)}/.."))
from arithmetic_overflow_violation import detect_arithmetic_overflow
from parse_verilog_fixtures import mini_verilog_sample, verilog_sample


@pytest.fixture
def verilog_snippet():
    return """
    reg [3:0]  try
    reg [3:0]  mry
    reg [3:0]  yry
    reg [2:0]  ry
    reg [1:0]  qry
    ry = yry + try
    """


def test_arithover_on_verilog_code_snippet(verilog_snippet):
    """Test detect_arithmetic_overflow() on verilog code snippet"""
    violations = detect_arithmetic_overflow(verilog_snippet)
    assert len(violations) == 1
    assert violations[0][0] == "ry"
    assert violations[0][1] == 7


def test_arithover_on_mini_verilog_sample(mini_verilog_sample):
    """Test detect_arithmetic_overflow() on mini_verilog_sample.v"""
    violations = detect_arithmetic_overflow(mini_verilog_sample)
    assert len(violations) == 2
    assert violations[0][0] == "reg_2"
    assert violations[0][1] == 66
    assert violations[1][0] == "reg_3"
    assert violations[1][1] == 72


def test_arithover_on_verilog_sample(verilog_sample):
    """Test detect_arithmetic_overflow() on verilog_sample.v"""
    violations = detect_arithmetic_overflow(verilog_sample)
    assert len(violations) == 4
    assert violations[0][0] == "reg_result_1"
    assert violations[0][1] == 104
    assert violations[1][0] == "reg_result_2"
    assert violations[1][1] == 109
    assert violations[2][0] == "reg_result_3"
    assert violations[2][1] == 114
    assert violations[3][0] == "reg_result_4"
    assert violations[3][1] == 119
