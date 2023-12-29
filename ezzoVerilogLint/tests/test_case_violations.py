"""
This module tests case_violations module functions on multiple verilog_samples
"""

import sys
import os

sys.path.append(os.path.realpath(f"{os.path.dirname(__file__)}/.."))
from case_violations import catch_non_full_case


with open(
    r"ezzoVerilogLint\tests\verilog_samples\verilog_sample.v", "r", encoding="utf-8"
) as f:
    verilog_code = f.read()

with open(
    r"ezzoVerilogLint\tests\verilog_samples\mini_verilog_sample.v",
    "r",
    encoding="utf-8",
) as f:
    mini_verilog_code = f.read()


def test_on_mini_verilog_sample():
    """Test catch_non_full_case() on mini_verilog_sample.v"""
    line_numbers = catch_non_full_case(mini_verilog_code)
    assert len(line_numbers) == 1
    assert line_numbers[0] == 4


def test_on_verilog_sample():
    """Test catch_non_full_case() on verilog_sample.v"""
    line_numbers = catch_non_full_case(verilog_code)
    assert len(line_numbers) == 1
    assert line_numbers[0] == 40
