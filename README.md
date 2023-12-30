# Verilog-Lint

In this project we will design static Verilog Design Checker, the checker will take Verilog (DUT) no Test Bench, and statically points to following List of Violations • Arithmetic Overflow • Unreachable Blocks • Unreachable FSM State • Un-initialized Register • Multi-Driven Bus/Register • Non Full/Parallel Case • Infer Latch

## CLI Usage

To run the package in the terminal and check for any violations inside a verilog file
```
usage: ezzoVerilogLint [-h] [-g] [-q] file_path [file_path ...]

Takes a verilog module file and checks for any violations

positional arguments:
  file_path       A path to verilog module .v, .sv or .txt file

options:
  -h, --help      show this help message and exit
  -g, --generate  Generate report.txt that contains the lint report in the current working directory
  -q, --quiet     Generate a report.txt without printing the report in the terminal
```
For example:
-  if you have a verilog file called verilog_sample.v in the current working directory and you want to just print the violations report in the terminal without generating any file `python -m ezzoVerilogLint verilog_sample.v`
-  You want to generate a report.txt for all the occurred violations in the current working directory in quiet mode `python -m ezzoVerilogLint -q -g verilog_sample.v`
