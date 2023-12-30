"""This module implements a function that catches infer latch violations in verilog file"""
import re


def check_infer_latch(verilog_code: str) -> list[int]:
    """Catch any inferred if-else blocks latches

    Arguments:
        verilog_code -- a string of verilog code

    Returns:
        line numbers where if blocks that infer latches occurred
    """
    iff = re.finditer(r"\bif\b", verilog_code)
    elsee = re.finditer(r"\belse\b", verilog_code)
    ifelse = list(iff)
    ifelse.extend(elsee)
    ifelse = sorted(ifelse, key=lambda x: x.start())
    iff = []
    for x in ifelse:
        if x.group() == "if":
            iff.append(x)
        else:
            iff.pop()

    line_numbers = []
    for x in iff:
        line_numbers.append(verilog_code.count("\n", 0, x.start()) + 1)

    return line_numbers
