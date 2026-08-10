from typing import Dict, List

from ct_platform.dependency_edge import DependencyEdge
from ct_platform.dependency_node import DependencyNode


class DependencyGraph:

    def __init__(self):

        self.nodes: Dict[str, DependencyNode] = {}
        self.edges: List[DependencyEdge] = []

        self.internal_imports = 0
        self.external_imports = 0
        self.unresolved_imports = 0

    def add_node(self, node: DependencyNode):

        self.nodes[node.id] = node

    def add_edge(self, edge: DependencyEdge):

        self.edges.append(edge)

    def node_count(self):

        return len(self.nodes)

    def edge_count(self):

        return len(self.edges)
