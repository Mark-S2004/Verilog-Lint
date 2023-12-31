"""
This module implements Report class
"""


class Report:
    def __init__(self, filename: str):
        self.filename = filename
        self.arithmetic_overflow_violations = []
        self.fullcase_violations = []
        self.parallelcase_violations = []
        self.infer_latch_violations = []
        self.multidriven_register_violations = []
        self.uninitialized_register_violations = []

    def __repr__(self) -> str:
        """
        Format example:
        Filename Lint Report
        ------------
        Arithmetic overflow violation on line number 5 for 'reg1' register
        No non full-case violations
        No non parallel-case violations
        No infer latch violations
        No multidriven register violations
        No uninitialized register violations
        """
        report = f"{self.filename} Lint Report\n------------"

        if not len(self.arithmetic_overflow_violations):
            report += "\nNo arithmetic overflow violation"
        else:
            report += "\nArithmetic Overflow violations:"
            for violation in self.arithmetic_overflow_violations:
                report += (
                    f"\n\tline number {violation[1]} for '{violation[0]}' register"
                )

        if not len(self.fullcase_violations):
            report += "\nNo non full-case violation"
        else:
            report += "\nNon full-case violations:"
            for line_numbers in self.fullcase_violations:
                report += f"\n\tline number {line_numbers} "

        if not len(self.parallelcase_violations):
            report += "\nNo non parallel case violation"
        else:
            report += "\nNon parallel-case violations:"
            for line_numbers in self.parallelcase_violations:
                report += f"\n\tline number {line_numbers} "

        if not len(self.infer_latch_violations):
            report += "\nNo latches infered"
        else:
            report += "\nInfer latch violations:"
            for line_numbers in self.infer_latch_violations:
                report += f"\n\tline number {line_numbers} "

        if not len(self.multidriven_register_violations):
            report += "\nNo multidriven register violation"
        else:
            report += "\nMultidriven register violation:"
            for duplicate in self.multidriven_register_violations:
                report += (
                    f"\n\tline number {list(duplicate)[1]} for {list(duplicate)[0]}"
                )

        if not len(self.uninitialized_register_violations):
            report += "\nNo uninitialized register violation"
        else:
            report += "\nUninitialized register:"
            for uninitialized_registers in self.uninitialized_register_violations:
                report += f"\n\ton line number {uninitialized_registers[0]} for register {uninitialized_registers[1]}"

        report += "\n\n"

        return report
