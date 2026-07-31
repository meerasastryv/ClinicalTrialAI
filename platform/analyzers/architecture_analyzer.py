"""
architecture_analyzer.py

Architecture Intelligence Analyzer
Refactored to use the PF-01 BaseAnalyzer framework.
"""

from collections import Counter

from platform.framework.base_analyzer import BaseAnalyzer
from platform.framework.analysis_result import AnalysisResult
from platform.models.dependency_graph import DependencyGraph
from platform.models.architecture_report import ArchitectureReport
from platform.analyzers.dependency_intelligence import (
    DependencyIntelligenceAnalyzer,
)

class ArchitectureAnalyzer(BaseAnalyzer):
    """
    Produces architecture intelligence from a dependency graph.
    """

    STANDARD_LIBRARY = {
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

    def __init__(self, context=None):
        super().__init__(context)
        self._graph = None
        self.dependency_intelligence_analyzer = (
            DependencyIntelligenceAnalyzer()
        )
    def execute(self, graph: DependencyGraph):
        """
        Convenience entry point for existing callers.
        """
        self._graph = graph
        return super().execute()

    #
    # ---------------------------------------------------------
    # BaseAnalyzer implementation
    # ---------------------------------------------------------
    #

    def collect(self):
        """
        Return the dependency graph supplied by execute().
        """
        if self._graph is None:
            raise ValueError("DependencyGraph has not been supplied.")
        return self._graph

    def analyze(
        self,
        graph: DependencyGraph,
        result: AnalysisResult,
    ):
        """
        Perform architecture analysis and populate AnalysisResult.
        """

        report = ArchitectureReport(
            engine_id=graph.engine_id
        )

        report.total_dependencies = len(graph.dependencies)

        report.circular_dependencies = graph.circular_dependencies

        fan_out = Counter()
        fan_in = Counter()

        internal = 0
        external = 0
        standard = 0

        #
        # Dependency statistics
        #
        for dep in graph.dependencies:

            fan_out[dep.source] += 1

            fan_in[dep.target] += 1

            if dep.target.startswith("src."):

                internal += 1

            elif dep.target.split(".")[0] in self.STANDARD_LIBRARY:

                standard += 1

            else:

                external += 1

        report.internal_dependencies = internal
        report.external_dependencies = external
        report.standard_library_dependencies = standard

        report.fan_in = dict(fan_in.most_common(10))
        report.fan_out = dict(fan_out.most_common(10))

        # ---------------------------------------------------------
        # Dependency Intelligence
        dependency_graph = {}
        for dep in graph.dependencies:
            dependency_graph.setdefault(dep.source,[]).append(dep.target)
        dependency_intelligence = (self.dependency_intelligence_analyzer.analyze(dependency_graph))
        report.dependency_intelligence = (    dependency_intelligence)
        # ---------------------------------------------------------
        # Architecture Health

        score = 100.0
        if report.circular_dependencies:
            score -= 25
            report.warnings.append(
                "Circular dependencies detected."
            )
        if report.total_dependencies > 0:
            ratio = (
                report.external_dependencies
                / report.total_dependencies
            )
            if ratio > 0.30:

                score -= 10

                report.warnings.append(
                    "High external dependency ratio."
                )

        if report.fan_out:

            highest = max(report.fan_out.values())

            if highest > 25:

                score -= 8

                report.warnings.append(
                    "Very high fan-out detected."
                )

        if report.fan_in:

            highest = max(report.fan_in.values())

            if highest > 40:

                score -= 5

                report.warnings.append(
                    "Very high fan-in detected."
                )

        score = max(score, 0)

        report.health_score = score

        if score >= 90:

            report.rating = "Excellent"

        elif score >= 80:

            report.rating = "Good"

        elif score >= 70:

            report.rating = "Fair"

        else:

            report.rating = "Needs Improvement"

        if report.rating == "Excellent":

            report.recommendations.append(
                "Architecture is healthy. Continue following the current layered design."
            )

        elif report.rating == "Good":

            report.recommendations.append(
                "Architecture is stable. Review high fan-in and fan-out modules."
            )

        else:

            report.recommendations.append(
                "Review architecture for coupling and dependency improvements."
            )

        #
        # Populate framework result
        #
        result.summary = {
            "engine_id": report.engine_id,
            "rating": report.rating,
            "health_score": report.health_score,
        }

        result.metrics = {
            "total_dependencies": report.total_dependencies,
            "internal_dependencies": report.internal_dependencies,
            "external_dependencies": report.external_dependencies,
            "standard_library_dependencies":
                report.standard_library_dependencies,
        }

        result.metadata["architecture_report"] = report

    def finalize(self, result: AnalysisResult):
        """
        Optional post-processing hook.
        """
        pass

    @staticmethod
    def get_report(result: AnalysisResult) -> ArchitectureReport:
        """
        Returns the strongly typed report stored in the AnalysisResult.
        """
        return result.metadata["architecture_report"]
