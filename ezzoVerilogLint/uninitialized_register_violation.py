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


if __name__ == "__main__":
    # Example usage:
    verilog_code = """
    reg [7:0] reg1, reg2 , reg3;
    wire [3:0] result ;
    result <= 4'b0101;
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            reg1 <= 8'b00000000;
            reg2 <= 8'b11110000;
        end else begin
            reg1 <= data_in + reg2;
            reg2 <= reg1;
        end

        // reg3 is uninitialized in this block
        result <= reg1 + reg2;
    end

    always @(posedge clk) begin
        // reg3 is uninitialized in this block
        data_out <= result + reg3;
        reg3 = 8'b01010101
    end
    """

    uninitialized_registers = check_uninitialized_registers(verilog_code)

    if uninitialized_registers:
        print("Uninitialized registers found:")
        for line_number, register_name in uninitialized_registers:
            print(f"Line {line_number}: {register_name}")
    else:
        print("No uninitialized registers found.")
