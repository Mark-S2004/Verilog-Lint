import re
from .global_functions import get_declared_regs


def evaluate_expression(expression, variables):
    expression = (
        expression.replace("\\", "")
        .replace("=", "==")
        .replace("+", "+")
        .replace("-", "-")
    )

    for var, python_var in variables.items():
        expression = re.sub(r"\b" + var + r"\b", str(python_var), expression)

    try:
        return eval(expression, {}, {"__builtins__": None})
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None


def detect_arithmetic_overflow(verilog):
    variable_bits = {}

    overflow_reg = r"\b(\w+)\s*=\s*(\w+)\s*[+\\-]\s*(\w+)\b"

    variable_declarations = get_declared_regs(verilog)

    for declaration in variable_declarations:
        variable_bits[declaration["name"]] = declaration["width"]

    overflow_matches = re.finditer(overflow_reg, verilog)

    violations = []
    for match in overflow_matches:
        var, operand1, operand2 = match.groups()
        if var in variable_bits:
            max_value = 2 ** variable_bits[var] - 1

            result1 = evaluate_expression(f"{operand1}", variable_bits)
            result2 = evaluate_expression(f"{operand2}", variable_bits)

            max_value_operands = 2 ** max(result1, result2) - 1

            if max_value_operands is not None and abs(max_value_operands) > max_value:
                lines = verilog.count("\n", 0, match.start()) + 1
                violations.append((var, lines))

    return violations
