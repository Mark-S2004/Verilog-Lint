"""
This module implements Veriloglint class
"""
import os
from Report import Report
from arithmetic_overflow_violation import detect_arithmetic_overflow
from case_violations import catch_non_full_case, catch_non_parallel_case
from infer_latch_violation import check_infer_latch
from multidriven_register_violation import check_multidriven_registers
from uninitialized_register_violation import check_uninitialized_registers


class Veriloglint:
    """Veriloglint class generates lint report and can

    Attributes:
        verilog_code (str): string of verilog module that was read from the file
                            in the path specified
        report (Report): A report that contains all violations found in the file and
                            the line number on which they occurred
    """

    def __init__(self, verilog_module_path: str):
        self._verilog_code = verilog_module_path
        self._report = self._verilog_code

    def __repr__(self) -> str:
        return repr(self.__report)

    @property
    def verilog_code(self) -> str:
        return self.__verilog_code

    @verilog_code.setter
    def _verilog_code(self, verilog_module_path):
        with open(verilog_module_path, "r", encoding="utf-8") as v:
            self.__verilog_code = v.read()

    @property
    def report(self) -> str:
        return repr(self.__report)

    @report.setter
    def _report(self, verilog_code: str):
        self.__report = Report()
        self.__report.arithmetic_overflow_violations = detect_arithmetic_overflow(
            verilog_code
        )
        self.__report.fullcase_violations = catch_non_full_case(verilog_code)
        self.__report.parallelcase_violations = catch_non_parallel_case(verilog_code)
        self.__report.infer_latch_violations = check_infer_latch(verilog_code)
        self.__report.multidriven_register_violations = check_multidriven_registers(
            verilog_code
        )
        self.__report.uninitialized_register_violations = check_uninitialized_registers(
            verilog_code
        )

    def generate_report(self, path: str = f"{os.getcwd()}/report.txt"):
        """Generate a report in

        Arguments:
            path -- Path including filename to generate or overwrite report in.
                    By defualt it is going to write in report.txt in the current working directory
        """
        with open(f"{path}", "w", encoding="utf-8") as report:
            report.write(repr(self.__report))
