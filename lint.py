import re

# Regular expressions for pattern matching
assignment_pattern = re.compile(r'\s*(\w+)\s*=\s*([^;]+);')
module_declaration_pattern = re.compile(r'\s*module\s+(\w+)\s*\(.*\);')
integer_declaration_pattern = re.compile(r'\s*reg\s+(signed\s+)?\[\w+:\w+\]\s+(\w+);')

# Class to represent a Verilog module
class VerilogModule:
    def __init__(self, name):
        self.name = name
        self.signals = {}
        self.assignments = []

    def add_signal(self, name):
        self.signals[name] = 0

    def add_assignment(self, signal, value):
        self.assignments.append((signal, value))

    def check_arithmetic_overflow(self):
        for signal, value in self.assignments:
            if isinstance(value, int) and value > (2 ** 31 - 1):
                print(f"Arithmetic Overflow detected in module '{self.name}', signal '{signal}'.")

    def check_uninitialized_registers(self):
        for signal, value in self.assignments:
            if value is None:
                print(f"Uninitialized Register detected in module '{self.name}', signal '{signal}'.")

    def check_infer_latch(self):
        for signal, value in self.assignments:
            if value is None:
                print(f"Infer Latch detected in module '{self.name}', signal '{signal}'.")

# Function to parse the Verilog code
def parse_verilog(verilog_code):
    modules = []
    current_module = None

    lines = verilog_code.split('\n')
    for line in lines:
        line = line.strip()

        if line.startswith('module'):
            match = module_declaration_pattern.match(line)
            if match:
                module_name = match.group(1)
                current_module = VerilogModule(module_name)
                modules.append(current_module)

        elif line.startswith('reg'):
            match = integer_declaration_pattern.match(line)
            if match and current_module:
                signal_name = match.group(2)
                current_module.add_signal(signal_name)

        elif ';' in line:
            match = assignment_pattern.match(line)
            if match and current_module:
                signal_name = match.group(1)
                value = match.group(2)
                if value.isdigit():
                    value = int(value)
                current_module.add_assignment(signal_name, value)

    return modules

# Example usage
verilog_code = """
module MyModule(input a, b, output y);
  reg [31:0] temp;
  reg [3:0] counter;

  assign y = a + b;

  always @(posedge clk) begin
    temp <= a + b;
    counter <= counter + 1;
  end
endmodule
"""

modules = parse_verilog(verilog_code)

for module in modules:
    module.check_arithmetic_overflow()
    module.check_uninitialized_registers()
    module.check_infer_latch()