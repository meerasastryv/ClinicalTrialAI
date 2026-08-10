"""
Graph Query Report
IC-05 - Knowledge Graph Engine
Milestone 10
"""

from pathlib import Path

from src.ic05.services.graph_query_engine import GraphQueryEngine


class GraphQueryReport:
    """
    Generates reports from the Knowledge Graph Query Engine.
    """

    def __init__(self, repository):
        self.query_engine = GraphQueryEngine(repository)

    # ---------------------------------------------------------

    def generate(
        self,
        output_file="output/ic05/graph_query_report.txt"
    ):
        """
        Generate the Graph Query Report.
        """

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        stats = self.query_engine.graph_statistics()

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as report:

            report.write(
                "GRAPH QUERY REPORT\n"
            )
            report.write(
                "=" * 70 + "\n\n"
            )

            report.write(
                "GRAPH SUMMARY\n"
            )
            report.write(
                "-" * 70 + "\n"
            )

            report.write(
                f"Total Nodes          : {stats.total_nodes}\n"
            )
            report.write(
                f"Total Edges          : {stats.total_edges}\n"
            )
            report.write(
                f"Average Degree       : {stats.average_degree:.2f}\n"
            )
            report.write(
                f"Isolated Nodes       : {stats.isolated_nodes}\n\n"
            )

            report.write(
                "NODE TYPES\n"
            )
            report.write(
                "-" * 70 + "\n"
            )

            if stats.node_types:

                for node_type, count in sorted(
                    stats.node_types.items()
                ):

                    report.write(
                        f"{node_type:<30}{count}\n"
                    )

            else:

                report.write(
                    "No node types found.\n"
                )

            report.write("\n")

            report.write(
                "RELATIONSHIP TYPES\n"
            )
            report.write(
                "-" * 70 + "\n"
            )

            if stats.relationship_types:

                for rel, count in sorted(
                    stats.relationship_types.items()
                ):

                    report.write(
                        f"{rel:<30}{count}\n"
                    )

            else:

                report.write(
                    "No relationships found.\n"
                )

            report.write("\n")

            report.write(
                "NODE DETAILS\n"
            )
            report.write(
                "-" * 70 + "\n"
            )

            nodes = sorted(
                self.query_engine.graph.get_all_nodes(),
                key=lambda n: n.node_id
            )

            for node in nodes:

                outgoing = self.query_engine.find_outgoing(
                    node.node_id
                )

                incoming = self.query_engine.find_incoming(
                    node.node_id
                )

                report.write(
                    f"\nNode ID   : {node.node_id}\n"
                )
                report.write(
                    f"Name      : {node.name}\n"
                )
                report.write(
                    f"Type      : {node.node_type}\n"
                )
                report.write(
                    f"Outgoing  : {len(outgoing)}\n"
                )
                report.write(
                    f"Incoming  : {len(incoming)}\n"
                )

                if outgoing:

                    report.write(
                        "Outgoing Relationships\n"
                    )

                    for edge in outgoing:

                        report.write(
                            f"   --> {edge.target} "
                            f"({edge.relationship})\n"
                        )

                if incoming:

                    report.write(
                        "Incoming Relationships\n"
                    )

                    for edge in incoming:

                        report.write(
                            f"   <-- {edge.source} "
                            f"({edge.relationship})\n"
                        )

        return output_file
