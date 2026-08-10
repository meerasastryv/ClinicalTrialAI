from collections import Counter

from ct_platform.models.dependency_graph import DependencyGraph


class DependencyAnalyzer:
    """
    Produces architecture statistics from a dependency graph.
    """

    def analyze(self, graph: DependencyGraph):

        internal = 0
        external = 0
        standard = 0

        source_counter = Counter()
        target_counter = Counter()

        stdlib = {
            "typing",
            "logging",
            "datetime",
            "collections",
            "json",
            "os",
            "pathlib",
            "uuid",
            "math",
            "time",
            "re",
            "ast",
            "dataclasses",
            "__future__",
        }

        for dep in graph.dependencies:

            source_counter[dep.source] += 1

            target_counter[dep.target] += 1

            if dep.target.startswith("src."):

                internal += 1

            elif dep.target.split(".")[0] in stdlib:

                standard += 1

            else:

                external += 1

        graph.statistics = {

            "total_dependencies": len(graph.dependencies),

            "internal_dependencies": internal,

            "external_dependencies": external,

            "standard_library_dependencies": standard,

            "most_dependent_file":

                source_counter.most_common(1),

            "most_imported_module":

                target_counter.most_common(1),
        }

        return graph
