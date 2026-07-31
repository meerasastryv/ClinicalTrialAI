from collections import defaultdict

from platform.models.dependency_graph import DependencyGraph


class CircularDependencyDetector:
    """
    Detects circular dependencies in a dependency graph.
    """

    def detect(self, graph: DependencyGraph):

        adjacency = defaultdict(set)

        # Build adjacency list using internal dependencies only
        for dep in graph.dependencies:

            if not dep.target.startswith("src."):
                continue

            source = dep.source.replace("\\", "/")
            target = dep.target.replace(".", "/") + ".py"

            adjacency[source].add(target)

        visited = set()
        stack = []
        cycles = []

        def dfs(node):

            if node in stack:

                index = stack.index(node)
                cycle = stack[index:] + [node]

                if cycle not in cycles:
                    cycles.append(cycle)

                return

            if node in visited:
                return

            visited.add(node)
            stack.append(node)

            for neighbour in adjacency.get(node, []):

                dfs(neighbour)

            stack.pop()

        for node in adjacency:

            dfs(node)

        graph.circular_dependencies = cycles

        return graph
