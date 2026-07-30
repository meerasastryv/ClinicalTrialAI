from dataclasses import dataclass, field
from typing import Dict, List

from platform.graph.dependency_edge import DependencyEdge
from platform.graph.dependency_node import DependencyNode


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

        self.edges.append(edge)

    def node_count(self):

        return len(self.nodes)

    def edge_count(self):

        return len(self.edges)

    def adjacency_list(self):

        graph = {}

        for edge in self.edges:
            graph.setdefault(edge.source, []).append(edge.target)

        return graph
