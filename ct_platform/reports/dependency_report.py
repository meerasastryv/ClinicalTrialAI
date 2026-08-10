"""
Dependency analysis reporter.

Generates Markdown, JSON and CSV reports for dependency analysis
results produced by the Platform Foundation.

Author: ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from ct_platform.reports.base_reporter import BaseReporter

logger = logging.getLogger(__name__)


class DependencyReporter(BaseReporter):
    """
    Reporter for dependency analysis results.
    """

    def build_report(
        self,
        analysis_result: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Return the report model.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        Returns
        -------
        dict[str, Any]
        """
        return analysis_result

    def generate_markdown(
        self,
        analysis_result: dict[str, Any],
        filename: str = "dependency_report",
    ) -> Path:
        """
        Generate Markdown report.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        filename
            Output filename without extension.

        Returns
        -------
        Path
        """
        markdown = self._build_markdown(analysis_result)
        return self.write_markdown(filename, markdown)

    def generate_json(
        self,
        analysis_result: dict[str, Any],
        filename: str = "dependency_report",
    ) -> Path:
        """
        Generate JSON report.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        filename
            Output filename without extension.

        Returns
        -------
        Path
        """
        return self.write_json(filename, analysis_result)

    def generate_csv(
        self,
        analysis_result: dict[str, Any],
        filename: str = "dependency_report",
    ) -> Path:
        """
        Generate CSV report.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        filename
            Output filename without extension.

        Returns
        -------
        Path
        """
        rows = self._build_csv_rows(analysis_result)
        return self.write_csv(filename, rows)

    def generate_reports(
        self,
        analysis_result: dict[str, Any],
        filename_prefix: str = "dependency_report",
    ) -> dict[str, Path]:
        """
        Generate all report formats.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        filename_prefix
            Base filename.

        Returns
        -------
        dict[str, Path]
        """
        logger.info("Generating dependency reports...")

        reports = {
            "markdown": self.generate_markdown(
                analysis_result,
                filename_prefix,
            ),
            "json": self.generate_json(
                analysis_result,
                filename_prefix,
            ),
            "csv": self.generate_csv(
                analysis_result,
                filename_prefix,
            ),
        }

        logger.info("Dependency reports generated successfully.")

        return reports

    def _build_markdown(
        self,
        analysis_result: dict[str, Any],
    ) -> str:
        """
        Build Markdown report.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        Returns
        -------
        str
        """
        summary = analysis_result.get("summary", {})
        statistics = analysis_result.get("statistics", {})
        dependencies = analysis_result.get("dependencies", [])
        violations = analysis_result.get("layer_violations", [])
        cycles = analysis_result.get("cycles", [])
        orphan_modules = analysis_result.get("orphan_modules", [])

        lines: list[str] = []

        lines.append("# Dependency Analysis Report")
        lines.append("")
        lines.append("## Summary")
        lines.append("")

        for key, value in summary.items():
            lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")

        lines.append("")
        lines.append("## Statistics")
        lines.append("")

        for key, value in statistics.items():
            lines.append(f"- **{key.replace('_', ' ').title()}**: {value}")

        lines.append("")
        lines.append("## Layer Violations")
        lines.append("")

        if violations:
            for violation in violations:
                lines.append(f"- {violation}")
        else:
            lines.append("No layer violations detected.")

        lines.append("")
        lines.append("## Cyclic Dependencies")
        lines.append("")

        if cycles:
            for cycle in cycles:
                lines.append(f"- {cycle}")
        else:
            lines.append("No cyclic dependencies detected.")

        lines.append("")
        lines.append("## Orphan Modules")
        lines.append("")

        if orphan_modules:
            for module in orphan_modules:
                lines.append(f"- {module}")
        else:
            lines.append("No orphan modules detected.")

        lines.append("")
        lines.append("## Dependency Details")
        lines.append("")

        if dependencies:
            lines.append("| Source | Target |")
            lines.append("|--------|--------|")

            for dependency in dependencies:
                source = dependency.get("source", "")
                target = dependency.get("target", "")
                lines.append(f"| {source} | {target} |")
        else:
            lines.append("No dependencies available.")

        return "\n".join(lines)

    def _build_csv_rows(
        self,
        analysis_result: dict[str, Any],
    ) -> list[dict[str, Any]]:
        """
        Convert dependency information to CSV rows.

        Parameters
        ----------
        analysis_result
            Dependency analysis results.

        Returns
        -------
        list[dict[str, Any]]
        """
        rows: list[dict[str, Any]] = []

        for dependency in analysis_result.get("dependencies", []):
            rows.append(
                {
                    "Source": dependency.get("source", ""),
                    "Target": dependency.get("target", ""),
                    "DependencyType": dependency.get(
                        "dependency_type",
                        "",
                    ),
                    "Layer": dependency.get("layer", ""),
                    "Status": dependency.get("status", ""),
                }
            )

        return rows
}
