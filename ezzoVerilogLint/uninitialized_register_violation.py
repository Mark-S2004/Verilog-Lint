import re

def check_uninitialized_registers(verilog_code):
    lines = verilog_code.split('\n')
    uninitialized_registers = []

    for i, line in enumerate(lines, start=1):
        # Check for lines containing reg or wire declarations
        if re.search(r'\b(?:reg|wire)\s+(\[\d+:\d+\])?\s*(\w+)\s*;', line):
            # Extract the register name
            match = re.search(r'\b(?:reg|wire)\s+(\[\d+:\d+\])?\s*(\w+)\s*;', line)
            if match:
                register_name = match.group(2)

                # Check if the register is assigned a value in the same line
                if not re.search(r'\b' + register_name + r'\s*=', line):
                    uninitialized_registers.append((i, register_name))

    return uninitialized_registers

if __name__ == "__main__":
    # Example usage:
    verilog_code = """
    reg [7:0] reg1, reg2, reg3;
    wire [3:0] result ;
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

    uninitialized_registers = check_uninitialized_registers(verilog_code)

    if uninitialized_registers:
        print("Uninitialized registers found:")
        for line_number, register_name in uninitialized_registers:
            print(f"Line {line_number}: {register_name}")
    else:
        print("No uninitialized registers found.")
