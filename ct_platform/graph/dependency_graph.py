from dataclasses import dataclass, field
from typing import Dict, List

from ct_platform.graph.dependency_edge import DependencyEdge
from ct_platform.graph.dependency_node import DependencyNode


@dataclass
class DependencyGraph:

    nodes: Dict[str, DependencyNode] = field(default_factory=dict)
    edges: List[DependencyEdge] = field(default_factory=list)

    internal_imports: int = 0
    external_imports: int = 0
    unresolved_imports: int = 0

    def add_node(self, node: DependencyNode):

        self.nodes[node.id] = node


    def add_edge(self, edge: DependencyEdge):
        """
        Add an edge to the graph and update node statistics.
        """
        self.edges.append(edge)
        if edge.source in self.nodes:
            self.nodes[edge.source].increment_outgoing()
        if edge.target in self.nodes:
            self.nodes[edge.target].increment_incoming()

    def node_count(self):

        return len(self.nodes)

    def edge_count(self):

        return len(self.edges)
    def adjacency_list(self):
        """
        Build adjacency list for graph traversal.
        """
        graph = {
            node_id: []
            for node_id in self.nodes}
        for edge in self.edges:
            graph[edge.source].append(edge.target)
        return graph
