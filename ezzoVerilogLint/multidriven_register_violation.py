import re
from global_functions import get_declared_regs
def check_multidriven_registers(verilog_code):
    # Extract register declarations
  
    registers = get_declared_regs(verilog_code)
    

    # Extract always blocks
    always_blocks = re.findall(r'\balways\b\s*?@\s*?\(.*?\).*?\bend\b', verilog_code, re.DOTALL)
    






    # Check each register in the always blocks
    for register in registers:
        assignments = []
        for block in always_blocks:
            if register["name"] in block:
                assign_stmts = re.findall(r'\b(\w+)\s*?<=', block)
                assignments.extend(assign_stmts)
                
    print("assignments",assignments)
    seen = set()
    duplicates = set()

    for item in assignments:
        if item in seen:
            duplicates.add(item)
        seen.add(item)

    
    

    return list(duplicates)


# Example usage
verilog_code = """
module example;
  reg a, b, c, d, e;

  always @(posedge clk)
  begin
    a <= b;
  end
  always @(posedge clk)
  begin
    b <= c;
  end
  always @(posedge clk)
  begin
    c <= d;
  end
  always @(posedge clk)
  begin
    b <= d;
  end
  always @(posedge clk)
  begin
    d <= e;
  end
  always @(posedge clk)
  begin
    a <= e;
  end

  always @(posedge clk)
  begin
    e <= c;
  end

endmodule
"""

multidriven_registers = check_multidriven_registers(verilog_code)
print("Multidriven registers:", multidriven_registers)
