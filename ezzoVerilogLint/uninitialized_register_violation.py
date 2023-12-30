from global_functions import get_declared_regs
import re


def check_uninitialized_registers(verilog_code):
    uninitialized_registers = []
    initialized_regs = []
    declared_registers = get_declared_regs(verilog_code)

    for each_reg in declared_registers:
        initialized_regs.append(
            {
                "name": each_reg["name"],
                "loc": re.finditer(r"\b" + each_reg["name"] + r"\s*<?=", verilog_code),
            }
        )

    appeared_regs = re.finditer(
        r"=\s*?(?P<left_operand>[a-zA-Z]\w*)(\s*?[+*-]\s*?(?P<right_operand>[a-zA-Z]\w*))?",
        verilog_code,
    )
    for appeared_reg in appeared_regs:
        found = False
        for initialized_reg in initialized_regs:
            if appeared_reg.group("left_operand") == initialized_reg["name"]:
                found = True
                for loc in initialized_reg["loc"]:
                    init = False
                    if loc.start() < appeared_reg.start():
                        init = True
                        break
                if not init:
                    uninitialized_registers.append(
                        (
                            verilog_code.count("\n", 0, appeared_reg.start()) + 1,
                            appeared_reg.group("left_operand"),
                        )
                    )
            if appeared_reg.group("right_operand") == initialized_reg["name"]:
                found = True
                for loc in initialized_reg["loc"]:
                    init = False
                    if loc.start() < appeared_reg.start():
                        init = True
                        break
                if not init:
                    uninitialized_registers.append(
                        (
                            verilog_code.count("\n", 0, appeared_reg.start()) + 1,
                            appeared_reg.group("right_operand"),
                        )
                    )
        if not found:
            uninitialized_registers.append(
                (
                    verilog_code.count("\n", 0, appeared_reg.start()) + 1,
                    appeared_reg.group("left_operand"),
                )
            )
    return uninitialized_registers
