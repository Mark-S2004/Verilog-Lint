import pytest


@pytest.fixture
def mini_verilog_sample():
    with open(
        r"ezzoVerilogLint\tests\verilog_samples\mini_verilog_sample.v",
        "r",
        encoding="utf-8",
    ) as f:
        mini_verilog_code = f.read()
    return mini_verilog_code


@pytest.fixture
def verilog_sample():
    with open(
        r"ezzoVerilogLint\tests\verilog_samples\verilog_sample.v", "r", encoding="utf-8"
    ) as f:
        verilog_code = f.read()
    return verilog_code
