"""
Execution Graph

Displays a simple execution tree based on collected runtime traces.
"""

from collections import defaultdict


class ExecutionGraph:
    """
    Builds and displays a simple execution tree.
    """

    def __init__(self, execution_traces=None):
        self.execution_traces = execution_traces or []

    def build_graph(self):
        """
        Build a parent -> children mapping.

        Expected trace attributes:
            parent_method
            method_name
        """

        graph = defaultdict(list)

        for trace in self.execution_traces:
            parent = getattr(trace, "parent_method", None)
            child = getattr(trace, "method_name", None)

            if parent and child:
                graph[parent].append(child)

        return graph

    def display(self):
        """
        Display execution graph.
        """

        graph = self.build_graph()

        print()
        print("=" * 60)
        print(" Execution Call Graph")
        print("=" * 60)

        if not graph:
            print("No execution trace available.")
            print("=" * 60)
            print()
            return

        visited = set()

        def print_node(node, level):
            indent = "    " * level

            if node in visited:
                return

            visited.add(node)

            print(f"{indent}{node}")

            for child in graph.get(node, []):
                print_node(child, level + 1)

        # Find root nodes
        children = set()

        for child_list in graph.values():
            children.update(child_list)

        roots = [node for node in graph.keys() if node not in children]

        if not roots:
            roots = list(graph.keys())

        for root in roots:
            print_node(root, 0)

        print("=" * 60)
        print()
