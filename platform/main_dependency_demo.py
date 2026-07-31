from pathlib import Path

from platform.services.dependency_graph_service import DependencyGraphService


engine_folder = Path("src/ic08")

service = DependencyGraphService()

graph = service.build(engine_folder)

print(f"\nDependency Graph for {graph.engine_id}\n")

for dependency in graph.dependencies:

    print(
        f"{dependency.source}"
        f" --> "
        f"{dependency.target}"
        f" ({dependency.dependency_type})"
    )
