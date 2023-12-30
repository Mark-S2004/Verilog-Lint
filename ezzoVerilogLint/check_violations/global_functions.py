"""
This module contains useful functions for the other modules
"""
import re


def get_declared_regs(verilog_code: str):
    reg_init_pattern = re.compile(
        r"(input|outupt)?\s*\b(reg|wire)\b\s*(\[\s*(?P<upper>\d+)\s*:\s*(?P<lower>\d+)\s*\])?\s*(?P<reg_name>\w+(\s*,\s*\w+)*)",
        re.MULTILINE,
    )
    regs = reg_init_pattern.finditer(verilog_code)
    regs_info = []
    for reg in regs:
        reg_info = dict.fromkeys(["name", "width", "line_no"])
        lower = reg.group("lower")
        upper = reg.group("upper")
        if upper is None:
            upper = 0
            lower = 0
        reg_info["width"] = (int(upper) - int(lower)) + 1
        reg_info["line_no"] = verilog_code.count("\n", 0, reg.start()) + 1
        names = [name.strip() for name in reg.group("reg_name").split(",")]
        for name in names:
            reg_info["name"] = name
            regs_info.append(reg_info.copy())

    return regs_info


if __name__ == "__main__":
    VERILOG_CODE = """
    reg [7:0] reg1,    reg2   , reg3;
    reg [3:0] result ;
    reg myReg;
    result = 4'b0101;
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
    end
    """

    reg_list = get_declared_regs(VERILOG_CODE)
    print(reg_list)
