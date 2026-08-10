"""
Layer Violation Reporter

Generates reports for detected architecture layer violations.
"""

from datetime import datetime


class LayerViolationReporter:
    """
    Generates reports for architecture layer violations.
    """

    def generate_report(self, violations):
        """
        Generate a formatted text report.

        Parameters
        ----------
        violations : List[LayerViolation]

        Returns
        -------
        str
        """

        report = []

        report.append("=" * 80)
        report.append("ARCHITECTURE LAYER VIOLATION REPORT")
        report.append("=" * 80)
        report.append(
            f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report.append("")

        if not violations:
            report.append("No layer violations detected.")
            report.append("")
            report.append("=" * 80)
            report.append("Architecture validation PASSED")
            report.append("=" * 80)

            return "\n".join(report)

        severity_count = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0
        }

        for index, violation in enumerate(violations, start=1):

            severity = violation.severity.upper()

            if severity not in severity_count:
                severity_count[severity] = 0

            severity_count[severity] += 1

            report.append("-" * 80)
            report.append(f"Violation #{index}")
            report.append("-" * 80)
            report.append(f"Source       : {violation.source}")
            report.append(f"Target       : {violation.target}")
            report.append(f"Source Layer : {violation.source_layer}")
            report.append(f"Target Layer : {violation.target_layer}")
            report.append(f"Rule         : {violation.rule_name}")
            report.append(f"Severity     : {violation.severity}")
            report.append(f"Description  : {violation.description}")
            report.append("")

        report.append("=" * 80)
        report.append("SUMMARY")
        report.append("=" * 80)
        report.append(f"Total Violations : {len(violations)}")
        report.append(f"Critical         : {severity_count.get('CRITICAL', 0)}")
        report.append(f"High             : {severity_count.get('HIGH', 0)}")
        report.append(f"Medium           : {severity_count.get('MEDIUM', 0)}")
        report.append(f"Low              : {severity_count.get('LOW', 0)}")

        report.append("")
        report.append("=" * 80)

        return "\n".join(report)

    def print_report(self, violations):
        """
        Print report to console.
        """

        print(self.generate_report(violations))

    def export_report(self, violations, output_file):
        """
        Export report to text file.
        """

        report = self.generate_report(violations)

        with open(output_file, "w", encoding="utf-8") as fp:
            fp.write(report)

        return output_file
