"""
Knowledge Graph Visualizer
IC-05 – Knowledge Graph Engine
Milestone 12 (Production Refactoring)
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable, List, Optional

logger = logging.getLogger(__name__)


class GraphVisualizer:
    """Provides formatted textual views of the Knowledge Graph."""

    def __init__(self, repository):
        self.graph = repository.get_graph()

    def _sorted_nodes(self) -> List:
        return sorted(self.graph.get_all_nodes(), key=lambda n: (n.node_type, n.node_id))

    def _format_node(self, node) -> str:
        return f"{node.node_id} [{node.node_type}] {node.name}"

    def _format_edges(self, node_id: str, relationship: Optional[str] = None) -> List[str]:
        lines = []
        for edge in self.graph.get_outgoing_edges(node_id):
            if relationship and edge.relationship != relationship:
                continue
            lines.append(f"   └── {edge.relationship} → {edge.target}")
        return lines

    def visualize(self) -> str:
        lines = ["Knowledge Graph", "=" * 80, ""]
        for node in self._sorted_nodes():
            lines.append(self._format_node(node))
            lines.extend(self._format_edges(node.node_id))
            lines.append("")
        return "\n".join(lines)

    def visualize_node(self, node_id: str) -> str:
        node = self.graph.get_node(node_id)
        if node is None:
            return f"Node '{node_id}' not found."
        lines = [self._format_node(node)]
        lines.extend(self._format_edges(node.node_id))
        return "\n".join(lines)

    def visualize_by_node_type(self, node_type: str) -> str:
        lines = [f"Nodes of type: {node_type}", "=" * 80]
        for node in self._sorted_nodes():
            if node.node_type == node_type:
                lines.append(self._format_node(node))
                lines.extend(self._format_edges(node.node_id))
                lines.append("")
        return "\n".join(lines)

    def visualize_by_relationship(self, relationship: str) -> str:
        lines = [f"Relationships: {relationship}", "=" * 80]
        for node in self._sorted_nodes():
            edges = self._format_edges(node.node_id, relationship)
            if edges:
                lines.append(self._format_node(node))
                lines.extend(edges)
                lines.append("")
        return "\n".join(lines)

    def summary(self) -> str:
        nodes = list(self.graph.get_all_nodes())
        edge_count = sum(len(self.graph.get_outgoing_edges(n.node_id)) for n in nodes)
        return (
            "Knowledge Graph Summary\n"
            + "=" * 80
            + f"\nTotal Nodes : {len(nodes)}"
            + f"\nTotal Edges : {edge_count}"
        )

    def export(self, output_file: str | Path) -> Path:
        path = Path(output_file)
        path.write_text(self.visualize(), encoding="utf-8")
        logger.info("Graph visualization exported to %s", path)
        return path
