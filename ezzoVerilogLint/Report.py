"""
This module implements Report class
"""


class Report:
    def __init__(self):
        self.arithmetic_overflow_violations = []
        self.fullcase_violations = []
        self.parallelcase_violations = []
        self.infer_latch_violations = []
        self.multidriven_register_violations = []
        self.uninitialized_register_violations = []

    def __repr__(self) -> str:
        """
        Format example:
        Lint Report
        ------------
        Arithmetic overflow violation on line number 5 for 'reg1' register
        No non full-case violations
        No non parallel-case violations
        No infer latch violations
        No multidriven register violations
        No uninitialized register violations
        """
        report = "Lint Report\n------------"

        if not len(self.arithmetic_overflow_violations):
            report += "\nNo arithmetic overflow violation"
        else:
            for violation in self.arithmetic_overflow_violations:
                report += f"\nArithmetic overflow violation on line number {violation[1]} for '{violation[0]}' register"

        if not len(self.fullcase_violations):
            report += "\nNo non full-case violation"
        else:
            for line_numbers in self.fullcase_violations:
                report += f"\nNon full case violation on line number {line_numbers} "

        if not len(self.parallelcase_violations):
            report += "\nNo non parallel case violation"
        else:
            for line_numbers in self.parallelcase_violations:
                report += (
                    f"\nNon parallel case violation on line number {line_numbers} "
                )

        if not len(self.infer_latch_violations):
            report += "\nNo latches infered"
        else:
            for line_numbers in self.infer_latch_violations:
                report += f"\nInfer latch violation on line number {line_numbers} "

        if not len(self.multidriven_register_violations):
            report += "\nNo multidriven register violation"
        else:
            for duplicate in self.multidriven_register_violations:
                report += f"\nMultidriven register violation {list(duplicate)}"

        if not len(self.uninitialized_register_violations):
            report += "\nNo uninitialized register violation"
        else:
            for uninitialized_registers in self.uninitialized_register_violations:
                report += f"\nUninitialized register found in line {uninitialized_registers[0]} for register {uninitialized_registers[1]}"

        return report
