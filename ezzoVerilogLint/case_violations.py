"""This module implements a function that catches non-fullcase violations in verilog file"""
import re
from global_functions import get_declared_regs


def catch_non_full_case(verilog_code: str) -> list[int]:
    """Catch any non full case, casex or casez statements and return their line numbers

    Arguments:
        verilog_code -- a string of verilog module code

    Returns:
        Returns a list of line numbers on which non full case, casex or casez statements occurred
    """
    line_numbers = []
    regs = get_declared_regs(verilog_code)

    case_pattern = re.compile(r"^[^/]*?\bcase[xz]?\b[\s\S]*?\bendcase\b", re.MULTILINE)
    case_expression_pattern = re.compile(r"\bcase[xz]?\b.*\(\s*(\w*)\s*\)")
    synthesis_directive_pattern = re.compile(r"//[\s\S]*\bfull_case\b")
    labels_pattern = re.compile(r"[;)]\s*(\d+'\w)?(?P<label>\w+)\s*:")
    default_pattern = re.compile(r"\bdefault\b")

    cases = case_pattern.finditer(verilog_code)
    for casee in cases:
        if synthesis_directive_pattern.search(casee.group()) or default_pattern.search(
            casee.group()
        ):
            continue

        case_expression = case_expression_pattern.search(casee.group()).group(1)
        case_expression_width = -1
        for reg in regs:
            if reg["name"] == case_expression:
                case_expression_width = reg["width"]
                break
        if case_expression_width == -1:
            continue
        possible_values = list(range(2**case_expression_width))

        labels = labels_pattern.finditer(casee.group())
        dont_care = False
        for label in labels:
            try:
                decimal_label = int(label.group("label"), 2)
            except ValueError:
                try:
                    decimal_label = int(label.group("label"))
                except ValueError:
                    dont_care = True
                    continue
            try:
                possible_values.remove(decimal_label)
            except ValueError:
                continue
        if dont_care:
            continue

        if not len(possible_values):
            continue

        line_numbers.append(verilog_code.count("\n", 0, casee.start()) + 1)

    return line_numbers

def catch_non_parallel_case(verilog_code: str) -> list[int]:
    """Catch any non parallel case, casex or casez statements and return their line numbers

    Arguments:
        verilog_code -- a string of verilog module code

    Returns:
        Returns a list of line numbers on which non parallel case, casex or casez statements occurred
    """
    line_numbers = []

    case_pattern = re.compile(r"^[^/]*?\bcase[xz]?\b[\s\S]*?\bendcase\b", re.MULTILINE)
    labels_pattern = re.compile(r"[;)]\s*(\d+'\w)?(?P<label>\w+)\s*:")

    cases = case_pattern.finditer(verilog_code)
    for casee in cases:
        parallel = True
        labels = labels_pattern.findall(casee.group())
        for label in labels:
            if sum(l[1]==label[1] for l in labels)>1:
                parallel = False
                break
        if not parallel:
            line_numbers.append(verilog_code.count("\n", 0, casee.start()) + 1)
    
    return line_numbers

if __name__ == "__main__":
    VERILOG_CODE = """reg [1:0] result;
    casez (result)
        1 : f = 2'b11;
        0: f=2'b10;
        0: f=2'b10;
        2'b10: f=2'b00;
    endcase
    """
    violations = catch_non_full_case(VERILOG_CODE)
    print(violations)

    violations = catch_non_parallel_case(VERILOG_CODE)
    print(violations)
