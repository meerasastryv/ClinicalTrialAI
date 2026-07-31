"""
analyzer_factory.py

Factory responsible for constructing analyzers.
"""

from .analyzer_registry import AnalyzerRegistry


class AnalyzerFactory:

    def __init__(self):

        self.registry = AnalyzerRegistry()

    def register(self, name, analyzer):

        self.registry.register(name, analyzer)

    def create(self, name):

        analyzer = self.registry.get(name)

        if analyzer is None:

            raise ValueError(
                f"Analyzer '{name}' is not registered."
            )

        return analyzer

    def names(self):

        return self.registry.names()
