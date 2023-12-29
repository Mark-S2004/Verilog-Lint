"""This module implements a function that catches infer latch violations in verilog file"""
import re

def check_infer_latch(test_code):
    iff = re.finditer(r"\bif\b", test_code)
    elsee = re.finditer(r"\belse\b", test_code)
    ifelse = list(iff)
    ifelse.extend(elsee)
    ifelse = sorted(ifelse, key=lambda x: x.start())
    iff = []
    for x in ifelse:
        if x.group() == "if":
            iff.append(x)
        else:
            iff.pop()
    for x in iff:
        line_number = test_code.count("\n", 0, x.start()) + 1
        print("Latch inferred at line:", line_number)

# Example usage
verilog_code = """
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

check_infer_latch(verilog_code)