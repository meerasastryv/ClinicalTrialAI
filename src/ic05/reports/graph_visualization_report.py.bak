"""
Graph Visualization Report
IC-05 – Knowledge Graph Engine
Milestone 12
"""

import os


class GraphVisualizationReport:
    """
    Generates a report for graph visualization exports.
    """

    def __init__(self, repository):
        self.graph = repository.get_graph()

    # ---------------------------------------------------------

    def generate(
        self,
        dot_file,
        mermaid_file,
        json_file
    ):
        """
        Generate visualization report.
        """

        lines = []

        lines.append("=" * 70)
        lines.append("GRAPH VISUALIZATION REPORT")
        lines.append("=" * 70)
        lines.append("")

        #
        # Graph statistics
        #

        lines.append("Graph Statistics")
        lines.append("-" * 70)

        lines.append(
            f"Total Nodes          : {len(self.graph.get_all_nodes())}"
        )

        lines.append(
            f"Total Relationships  : {len(self.graph.get_all_edges())}"
        )

        lines.append("")

        #
        # Exported Files
        #

        lines.append("Exported Files")
        lines.append("-" * 70)

        self._add_file(lines, dot_file)
        self._add_file(lines, mermaid_file)
        self._add_file(lines, json_file)

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    # ---------------------------------------------------------

    def _add_file(self, lines, filename):

        if os.path.exists(filename):

            size = os.path.getsize(filename)

            lines.append(
                f"{filename} ({size} bytes)"
            )

        else:

            lines.append(
                f"{filename} (Not Generated)"
            )
