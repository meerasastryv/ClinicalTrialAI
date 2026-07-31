from dataclasses import dataclass, field
from typing import Dict, List

from platform.models.dependency import Dependency


@dataclass
class DependencyGraph:
    """
    Represents all dependencies within an engine.
    """

    engine_id: str

    dependencies: List[Dependency] = field(default_factory=list)

    statistics: Dict = field(default_factory=dict)

    circular_dependencies: List[List[str]] = field(default_factory=list)

    def add(self, dependency: Dependency):
        self.dependencies.append(dependency)
