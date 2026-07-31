from pathlib import Path

from platform.services.circular_dependency_detector import (
    CircularDependencyDetector,
)
from platform.services.dependency_graph_service import (
    DependencyGraphService,
)

engine = Path("src/ic08")

graph = DependencyGraphService().build(engine)

graph = CircularDependencyDetector().detect(graph)

print("\n========== Circular Dependency Analysis ==========\n")

if not graph.circular_dependencies:

    print("No circular dependencies found.")

else:

    for i, cycle in enumerate(graph.circular_dependencies, start=1):

        print(f"\nCycle {i}")

        for node in cycle:

            print(f"   {node}")
