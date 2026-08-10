import ast
from pathlib import Path

from ct_platform.models.dependency import Dependency
from ct_platform.models.dependency_graph import DependencyGraph


class DependencyGraphService:
    """
    Builds a dependency graph for an Intelligence Component.
    """

    def build(self, engine_folder: Path) -> DependencyGraph:

        graph = DependencyGraph(
            engine_id=engine_folder.name.upper()
        )

        for py_file in engine_folder.rglob("*.py"):

            source = py_file.relative_to(engine_folder).as_posix()

            try:

                with open(py_file, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())

            except Exception:
                continue

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        graph.add(
                            Dependency(
                                source=source,
                                target=alias.name,
                                dependency_type="import",
                            )
                        )

                elif isinstance(node, ast.ImportFrom):

                    module = node.module or ""

                    graph.add(
                        Dependency(
                            source=source,
                            target=module,
                            dependency_type="from-import",
                        )
                    )

        return graph
