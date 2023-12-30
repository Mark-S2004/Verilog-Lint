"""
This module tests case_violations module functions on multiple verilog_samples
"""

import sys
import os

import pytest

sys.path.append(os.path.realpath(f"{os.path.dirname(__file__)}/.."))
from uninitialized_register_violation import check_uninitialized_registers
from parse_verilog_fixtures import mini_verilog_sample, verilog_sample


@pytest.fixture
def verilog_snippet():
    return """
    reg [7:0] reg1, reg2 , reg3;
    reg [3:0] result ;
    result <= 4'b0101;
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            reg1 <= 8'b00000000;
            reg2 <= 8'b11110000;
        end else begin
            reg1 <= data_in + reg2;
            reg2 <= reg1;
        end

        result <= reg1 + reg2;
    end

    always @(posedge clk) begin
        // reg3 is uninitialized in this block
        data_out <= result + reg3;
        reg3 = 8'b01010101
    end
    """


def test_uninitreg_on_verilog_code_snippet(verilog_snippet):
    """Test check_uninitialized_registers() on verilog code snippet"""
    violations = check_uninitialized_registers(verilog_snippet)
    assert len(violations) == 2
    assert violations[0][0] == 10
    assert violations[0][1] == "data_in"
    assert violations[1][0] == 19
    assert violations[1][1] == "reg3"


def test_uninitreg_on_mini_verilog_sample(mini_verilog_sample):
    """Test check_uninitialized_registers() on mini_verilog_sample.v"""
    violations = check_uninitialized_registers(mini_verilog_sample)
    assert len(violations) == 2
    assert violations[0][0] == 41
    assert violations[0][1] == "reg3"
    assert violations[1][0] == 41
    assert violations[1][1] == "reg4"


def test_uninitreg_on_verilog_sample(verilog_sample):
    """Test check_uninitialized_registers() on verilog_sample.v"""
    violations = check_uninitialized_registers(verilog_sample)
    assert len(violations) == 5
    assert violations[0][0] == 11
    assert violations[0][1] == "b"
    assert violations[1][0] == 18
    assert violations[1][1] == "data_in"
    assert violations[2][0] == 50
    assert violations[2][1] == "c"
    assert violations[3][0] == 53
    assert violations[3][1] == "reg3"
    assert violations[4][0] == 76
    assert violations[4][1] == "d"
