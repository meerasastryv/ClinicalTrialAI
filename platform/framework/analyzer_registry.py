"""
analyzer_registry.py

Registry for Platform Foundation analyzers.
"""

from typing import Dict, List

from .base_analyzer import BaseAnalyzer


class AnalyzerRegistry:
    """
    Registry of all available analyzers.
    """

    def __init__(self):

        self._analyzers: Dict[str, BaseAnalyzer] = {}

    def register(
        self,
        name: str,
        analyzer: BaseAnalyzer,
    ):

        self._analyzers[name] = analyzer

    def unregister(self, name: str):

        self._analyzers.pop(name, None)

    def get(self, name: str):

        return self._analyzers.get(name)

    def names(self) -> List[str]:

        return sorted(self._analyzers.keys())

    def analyzers(self):

        return self._analyzers.items()

    def clear(self):

        self._analyzers.clear()

    def __len__(self):

        return len(self._analyzers)

    def __contains__(self, name):

        return name in self._analyzers
