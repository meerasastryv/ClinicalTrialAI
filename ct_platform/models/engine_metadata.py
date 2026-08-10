from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class EngineMetadata:

    engine_id: str

    name: str

    version: str = "1.0"

    description: str = ""

    author: str = ""

    enabled: bool = True

    services: List[str] = field(default_factory=list)

    repositories: List[str] = field(default_factory=list)

    models: List[str] = field(default_factory=list)

    generators: List[str] = field(default_factory=list)

    analyzers: List[str] = field(default_factory=list)

    main_files: List[str] = field(default_factory=list)

    readme: bool = False

    file_count: int = 0

    dependencies: List[str] = field(default_factory=list)

    tags: List[str] = field(default_factory=list)

    config: Dict = field(default_factory=dict)
