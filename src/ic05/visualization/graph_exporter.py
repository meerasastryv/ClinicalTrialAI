"""
Knowledge Graph Exporter
IC-05 – Knowledge Graph Engine
Milestone 12
"""

import json
import os


class GraphExporter:
    """
    Exports the Knowledge Graph into multiple formats.
    """

    def __init__(self, repository):
        self.graph = repository.get_graph()

    # ---------------------------------------------------------

    def export_dot(self, filename):
        """
        Export GraphViz DOT format.
        """

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:

            f.write("digraph KnowledgeGraph {\n")
            f.write("    rankdir=LR;\n")
            f.write("\n")

            #
            # Nodes
            #
            for node in self.graph.get_all_nodes():

                label = f"{node.node_id}\\n{node.node_type}"

                f.write(
                    f'    "{node.node_id}" '
                    f'[label="{label}"];\n'
                )

            f.write("\n")

            #
            # Edges
            #
            for edge in self.graph.get_all_edges():

                f.write(
                    f'    "{edge.source}" -> "{edge.target}" '
                    f'[label="{edge.relationship}"];\n'
                )

            f.write("}\n")

    # ---------------------------------------------------------

    def export_mermaid(self, filename):
        """
        Export Mermaid format.
        """

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:

            f.write("graph LR\n")

            for edge in self.graph.get_all_edges():

                f.write(
                    f'    {edge.source}'
                    f'--|{edge.relationship}|'
                    f'{edge.target}\n'
                )

    # ---------------------------------------------------------

    def export_json(self, filename):
        """
        Export JSON representation.
        """

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        data = {
            "nodes": [],
            "edges": []
        }

        for node in self.graph.get_all_nodes():

            data["nodes"].append({
                "id": node.node_id,
                "type": node.node_type,
                "name": node.name
            })

        for edge in self.graph.get_all_edges():

            data["edges"].append({
                "source": edge.source,
                "target": edge.target,
                "relationship": edge.relationship
            })

        with open(filename, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4
            )
