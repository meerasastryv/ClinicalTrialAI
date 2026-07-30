from platform.graph.dependency_graph import DependencyGraph


class CycleDetector:

    def __init__(self, graph: DependencyGraph):

        self.graph = graph
        self.graph_map = graph.adjacency_list()

        self.visited = set()
        self.stack = set()
        self.cycles = []

    def detect(self):

        for node in self.graph.nodes:

            if node not in self.visited:
                self._dfs(node, [])

        return self.cycles

    def _dfs(self, node, path):

        self.visited.add(node)
        self.stack.add(node)

        path.append(node)

        for neighbour in self.graph_map.get(node, []):

            if neighbour not in self.visited:

                self._dfs(neighbour, path.copy())

            elif neighbour in self.stack:

                idx = path.index(neighbour)
                self.cycles.append(path[idx:] + [neighbour])

        self.stack.remove(node)
