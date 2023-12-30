import re
from global_functions import get_declared_regs


def find_occurrences(string, register_name):
    pattern = rf"\b{re.escape(register_name)}\s*?<=\s*"
    return [match.start() for match in re.finditer(pattern, string)]


def check_multidriven_registers(verilog_code):
    # Extract register declarations
    registers = get_declared_regs(verilog_code)

    # Extract always blocks
    always_blocks = re.findall(
        r"\balways\b\s*?@\s*?\(.*?\).*?\bend\b", verilog_code, re.DOTALL
    )

    multidriven_registers = []

    # Check each register in the always blocks
    for register in registers:
        occurrences = []

        for block in always_blocks:
            if register["name"] in block:
                occurrences.extend(find_occurrences(verilog_code, register["name"]))

        if len(set(occurrences)) > 1:
            for occurrence in set(occurrences):
                line_number = verilog_code.count("\n", 0, occurrence) + 1
                multidriven_registers.append((register["name"], line_number))

    return multidriven_registers
