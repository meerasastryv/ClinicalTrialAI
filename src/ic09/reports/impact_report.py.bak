"""
Impact Report

Generates a human-readable report from an impact analysis.

Author: ClinicalTrialAI
"""

from typing import List

from src.ic09.models.impact_result import ImpactResult
from src.ic09.models.impact_node import ImpactNode


class ImpactReport:
    """
    Builds a text report for an impact analysis.
    """

    def generate(self, result: ImpactResult) -> str:
        """
        Generate a formatted report.
        """
        lines: List[str] = []

        lines.append("=" * 70)
        lines.append("IMPACT ANALYSIS REPORT")
        lines.append("=" * 70)

        lines.append(f"Analysis ID     : {result.analysis_id}")
        lines.append(f"Source Artifact : {result.source_artifact}")
        lines.append(f"Source Type     : {result.source_type}")
        lines.append(f"Risk Score      : {result.risk_score:.2f}")
        lines.append(f"Execution Time  : {result.execution_time:.4f} sec")
        lines.append(f"Total Impacts   : {result.total_impacts}")

        lines.append("")
        lines.append("-" * 70)
        lines.append("IMPACTED ARTIFACTS")
        lines.append("-" * 70)

        if not result.impacted_nodes:
            lines.append("No impacted artifacts discovered.")
        else:
            for index, node in enumerate(result.impacted_nodes, start=1):
                lines.append(self._format_node(index, node))

        lines.append("")
        lines.append("-" * 70)
        lines.append("RELATIONSHIPS")
        lines.append("-" * 70)

        if not result.relationships:
            lines.append("No relationships recorded.")
        else:
            for edge in result.relationships:
                lines.append(
                    f"{edge.source_id} "
                    f"--[{edge.relationship}]--> "
                    f"{edge.target_id}"
                )

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    @staticmethod
    def _format_node(index: int, node: ImpactNode) -> str:
        """
        Format a single impacted node.
        """
        return (
            f"{index:02d}. "
            f"[{node.node_type}] "
            f"{node.name} "
            f"(Severity={node.severity}, "
            f"Confidence={node.confidence:.2f})"
        )
