"""
Dependency Intelligence Analyzer

Calculates architectural intelligence over the dependency graph.

Author: ClinicalTrialAI Platform
"""

from collections import defaultdict
from typing import Dict, List, Set

from platform.models.dependency_intelligence import (
    DependencyIntelligence,
    ModuleMetrics,
    CircularDependency,
    Hotspot,
)


class DependencyIntelligenceAnalyzer:
    """
    Calculates architectural intelligence metrics.
    """

    def analyze(self, dependency_graph) -> DependencyIntelligence:
        """
        Analyze a dependency graph.

        Expected graph format:

        {
            "moduleA": ["moduleB", "moduleC"],
            "moduleB": ["moduleC"]
        }
        """

        intelligence = DependencyIntelligence()

        if not dependency_graph:
            return intelligence

        metrics = self._build_metrics(dependency_graph)

        cycles = self._find_cycles(dependency_graph)

        self._mark_cycles(metrics, cycles)

        self._calculate_instability(metrics)

        self._calculate_risk(metrics)

        hotspots = self._identify_hotspots(metrics)

        recommendations = self._generate_recommendations(
            metrics,
            cycles,
            hotspots,
        )

        intelligence.module_metrics = metrics
        intelligence.circular_dependencies = cycles
        intelligence.hotspots = hotspots
        intelligence.recommendations = recommendations

        return intelligence

    # -------------------------------------------------------------

    def _build_metrics(
        self,
        graph: Dict[str, List[str]],
    ) -> Dict[str, ModuleMetrics]:

        metrics = {}

        reverse_graph = defaultdict(list)

        for source, targets in graph.items():

            if source not in metrics:
                metrics[source] = ModuleMetrics(name=source)

            metrics[source].dependencies = list(targets)

            metrics[source].fan_out = len(targets)

            for target in targets:

                reverse_graph[target].append(source)

                if target not in metrics:
                    metrics[target] = ModuleMetrics(name=target)

        for module, dependents in reverse_graph.items():

            metrics[module].dependents = dependents

            metrics[module].fan_in = len(dependents)

        return metrics

    # -------------------------------------------------------------

    def _calculate_instability(
        self,
        metrics: Dict[str, ModuleMetrics],
    ):

        for module in metrics.values():

            total = module.fan_in + module.fan_out

            if total == 0:
                module.instability = 0.0
            else:
                module.instability = round(
                    module.fan_out / total,
                    2,
                )

    # -------------------------------------------------------------

    def _calculate_risk(
        self,
        metrics: Dict[str, ModuleMetrics],
    ):

        for module in metrics.values():

            if module.in_cycle:
                module.risk = "CRITICAL"

            elif module.fan_out >= 20:
                module.risk = "HIGH"

            elif module.fan_in >= 30:
                module.risk = "HIGH"

            elif module.fan_out >= 10:
                module.risk = "MEDIUM"

            else:
                module.risk = "LOW"

    # -------------------------------------------------------------

    def _identify_hotspots(
        self,
        metrics: Dict[str, ModuleMetrics],
    ) -> List[Hotspot]:

        hotspots = []

        for module in metrics.values():

            score = (
                module.fan_in
                + module.fan_out
                + (20 if module.in_cycle else 0)
            )

            if score > 10:

                reason = (
                    f"FanIn={module.fan_in}, "
                    f"FanOut={module.fan_out}, "
                    f"Cycle={module.in_cycle}"
                )

                hotspots.append(
                    Hotspot(
                        module=module.name,
                        score=score,
                        reason=reason,
                    )
                )

        hotspots.sort(
            key=lambda h: h.score,
            reverse=True,
        )

        return hotspots

    # -------------------------------------------------------------

    def _find_cycles(
        self,
        graph: Dict[str, List[str]],
    ) -> List[CircularDependency]:

        visited: Set[str] = set()

        stack: List[str] = []

        cycles = []

        def dfs(node):

            if node in stack:

                idx = stack.index(node)

                cycle = stack[idx:] + [node]

                cycles.append(
                    CircularDependency(
                        modules=cycle
                    )
                )

                return

            if node in visited:
                return

            visited.add(node)

            stack.append(node)

            for child in graph.get(node, []):

                dfs(child)

            stack.pop()

        for node in graph:

            dfs(node)

        return cycles

    # -------------------------------------------------------------

    def _mark_cycles(
        self,
        metrics: Dict[str, ModuleMetrics],
        cycles: List[CircularDependency],
    ):

        for cycle in cycles:

            for module in cycle.modules:

                if module in metrics:
                    metrics[module].in_cycle = True

    # -------------------------------------------------------------

    def _generate_recommendations(
        self,
        metrics,
        cycles,
        hotspots,
    ) -> List[str]:

        recommendations = []

        if cycles:

            recommendations.append(
                "Break circular dependencies."
            )

        if hotspots:

            recommendations.append(
                "Refactor architectural hotspots."
            )

        for module in metrics.values():

            if module.fan_out >= 20:

                recommendations.append(
                    f"Reduce coupling in '{module.name}'."
                )

            if module.fan_in >= 30:

                recommendations.append(
                    f"Review impact before modifying '{module.name}'."
                )

        return sorted(set(recommendations))
