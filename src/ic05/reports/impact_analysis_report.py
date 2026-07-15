"""
Impact Analysis Report
IC-05 – Knowledge Graph Engine
Milestone 11
"""

from pathlib import Path

from src.ic05.services.impact_analysis_engine import (
    ImpactAnalysisEngine,
)


class ImpactAnalysisReport:
    """
    Generates an Impact Analysis Report.
    """

    def __init__(self, repository):
        self.engine = ImpactAnalysisEngine(repository)

    # ---------------------------------------------------------

    def generate(
        self,
        source_node,
        output_file="output/ic05/impact_analysis_report.txt",
    ):
        """
        Generate impact analysis report.
        """

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        result = self.engine.analyze(source_node)

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as report:

            report.write("IMPACT ANALYSIS REPORT\n")
            report.write("=" * 70 + "\n\n")

            report.write(f"Source Node : {result.source_node}\n")
            report.write(
                f"Impact Score : {result.impact_score:.2f}\n"
            )
            report.write(
                f"Blast Radius : {result.blast_radius}\n"
            )
            report.write(
                f"Dependency Depth : {result.dependency_depth}\n"
            )
            report.write(
                f"Total Impacted Nodes : "
                f"{result.total_impacted_nodes}\n"
            )

            report.write("\n")

            self._write_section(
                report,
                "DIRECT DEPENDENCIES",
                result.direct_dependencies,
            )

            self._write_section(
                report,
                "INDIRECT DEPENDENCIES",
                result.indirect_dependencies,
            )

            self._write_section(
                report,
                "IMPACTED REQUIREMENTS",
                result.impacted_requirements,
            )

            self._write_section(
                report,
                "IMPACTED CLASSES",
                result.impacted_classes,
            )

            self._write_section(
                report,
                "IMPACTED METHODS",
                result.impacted_methods,
            )

            self._write_section(
                report,
                "IMPACTED APIs",
                result.impacted_apis,
            )

            self._write_section(
                report,
                "IMPACTED DATABASES",
                result.impacted_databases,
            )

            self._write_section(
                report,
                "ALL IMPACTED NODES",
                result.impacted_nodes,
            )

        return output_file

    # ---------------------------------------------------------

    @staticmethod
    def _write_section(
        report,
        title,
        values,
    ):
        """
        Write a report section.
        """

        report.write(title + "\n")
        report.write("-" * 70 + "\n")

        if values:

            for value in sorted(set(values)):
                report.write(f"- {value}\n")

        else:

            report.write("None\n")

        report.write("\n")

    # ---------------------------------------------------------

    def print_summary(
        self,
        source_node,
    ):
        """
        Print a console summary.
        """

        result = self.engine.analyze(source_node)

        print("=" * 70)
        print("IMPACT ANALYSIS")
        print("=" * 70)

        print(f"Source Node         : {result.source_node}")
        print(f"Impact Score        : {result.impact_score:.2f}")
        print(f"Blast Radius        : {result.blast_radius}")
        print(f"Dependency Depth    : {result.dependency_depth}")
        print(f"Impacted Nodes      : {result.total_impacted_nodes}")

        print("=" * 70)
