import sys
import os
import argparse

from tensorboard import program
from .Veriloglint import Veriloglint

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1:
        print("Welcome to ezzoVerilogLint")
        print(
            "To use the lint pass one or more verilog module .v, .sv or .txt file paths"
        )
    if num_args >= 2:
        parser = argparse.ArgumentParser(
            prog="ezzoVerilogLint",
            description="Takes a verilog module file and checks for any violations",
        )
        parser.add_argument(
            "filepath",
            metavar="file_path",
            nargs="+",
            help="A path to verilog module .v, .sv or .txt file",
        )
        parser.add_argument(
            "-g",
            "--generate",
            action="store_true",
            help="Generate report.txt that contains the lint report in the current working directory",
        )
        parser.add_argument(
            "-q",
            "--quiet",
            action="store_true",
            help="Generate a report.txt without printing the report in the terminal",
        )

        args = parser.parse_args()
        for file_path in args.filepath:
            if os.path.isfile(file_path) and (
                file_path.endswith(".v")
                or file_path.endswith(".sv")
                or file_path.endswith(".txt")
            ):
                lint = Veriloglint(file_path)
                if not args.quiet:
                    print(lint)
                if args.generate:
                    lint.generate_report()
            else:
                print(f"{file_path} is not a valid verilog module file path")
