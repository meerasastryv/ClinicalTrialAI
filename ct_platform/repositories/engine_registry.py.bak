from typing import Dict, List

from ct_platform.models.engine_metadata import EngineMetadata


class EngineRegistry:
    """
    Stores metadata for all registered Intelligence Components.
    """

    def __init__(self):
        self._engines: Dict[str, EngineMetadata] = {}

    def register(self, metadata: EngineMetadata):
        self._engines[metadata.engine_id] = metadata

    def unregister(self, engine_id: str):
        self._engines.pop(engine_id, None)

    def get(self, engine_id: str):
        return self._engines.get(engine_id)

    def list_all(self) -> List[EngineMetadata]:
        return list(self._engines.values())

    def exists(self, engine_id: str):
        return engine_id in self._engines

    def clear(self):
        self._engines.clear()
