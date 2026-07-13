"""
relationship_report.py

Generates reports for graph relationships stored in the
RelationshipRepository.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Dict


class RelationshipReport:
    """
    Generates relationship reports from the repository.
    """

    def __init__(self, repository):
        self.repository = repository

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Returns repository statistics.
        """

        return self.repository.get_statistics()

    def relationship_type_counts(self) -> Dict[str, int]:
        """
        Count relationships by type.
        """

        counter = Counter()

        for relationship in self.repository.get_all_relationships():
            counter[relationship.relationship_type] += 1

        return dict(counter)

    def top_connected_nodes(self, top_n: int = 10):
        """
        Returns the most connected nodes.
        """

        counter = Counter()

        for relationship in self.repository.get_all_relationships():

            counter[relationship.source_id] += 1
            counter[relationship.target_id] += 1

        return counter.most_common(top_n)

    # ------------------------------------------------------------------
    # Report Generation
    # ------------------------------------------------------------------

    def generate_text_report(self) -> str:
        """
        Generate a formatted text report.
        """

        stats = self.statistics()

        lines = []

        lines.append("=" * 70)
        lines.append("GRAPH RELATIONSHIP REPORT")
        lines.append("=" * 70)
        lines.append("")

        lines.append(
            f"Total Relationships : "
            f"{stats['total_relationships']}"
        )

        lines.append(
            f"Unique Sources      : "
            f"{stats['unique_sources']}"
        )

        lines.append(
            f"Unique Targets      : "
            f"{stats['unique_targets']}"
        )

        lines.append("")

        lines.append("Relationship Types")
        lines.append("-" * 70)

        for relationship_type, count in sorted(
            self.relationship_type_counts().items()
        ):

            lines.append(
                f"{relationship_type:<30} {count:>8}"
            )

        lines.append("")
        lines.append("Top Connected Nodes")
        lines.append("-" * 70)

        for node, count in self.top_connected_nodes():

            lines.append(
                f"{node:<35} {count:>5}"
            )

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    def generate_json_report(self) -> Dict:
        """
        Generate report as dictionary.
        """

        return {
            "statistics": self.statistics(),
            "relationship_types": self.relationship_type_counts(),
            "top_connected_nodes": self.top_connected_nodes(),
        }

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------

    def save_text_report(self, output_file: str):
        """
        Save report to text file.
        """

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            self.generate_text_report(),
            encoding="utf-8",
        )

    def save_json_report(self, output_file: str):
        """
        Save report as JSON.
        """

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_path.open(
            "w",
            encoding="utf-8",
        ) as fp:

            json.dump(
                self.generate_json_report(),
                fp,
                indent=4,
            )

    # ------------------------------------------------------------------
    # Console
    # ------------------------------------------------------------------

    def print_report(self):
        """
        Print report to console.
        """

        print(self.generate_text_report())
