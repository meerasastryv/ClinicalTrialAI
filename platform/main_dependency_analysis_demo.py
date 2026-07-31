from pathlib import Path

from platform.services.dependency_analyzer import DependencyAnalyzer
from platform.services.dependency_graph_service import DependencyGraphService


engine = Path("src/ic08")

graph = DependencyGraphService().build(engine)

graph = DependencyAnalyzer().analyze(graph)

print("\n========== Dependency Analysis ==========\n")

for key, value in graph.statistics.items():

    print(f"{key:35} : {value}")
