"""
This module implements Report class
"""


from ezzoVerilogLint import arithmetic_overflow_violation


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
            report += "\nNo arithmetic overflow violations"
        else:
            for violation in self.arithmetic_overflow_violations:
                report += f"\nArithmetic overflow violation on line number {violation[1]} for '{violation[0]}' register"

        return report
