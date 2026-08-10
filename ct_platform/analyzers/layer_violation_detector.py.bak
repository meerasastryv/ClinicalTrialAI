"""
Layer Violation Detector

Traverses the architecture graph and detects
layer rule violations.
"""

from ct_platform.models.layer_violation import LayerViolation
from ct_platform.services.layer_rule_service import LayerRuleService


class LayerViolationDetector:
    """
    Detects architecture layer violations.
    """

    def __init__(self):

        self.rule_service = LayerRuleService()
    def detect(self, dependency_graph):
        """
        Detect architecture layer violations.
        Parameters
        ----------
        dependency_graph : DependencyGraph
        Returns
        -------
        List[LayerViolation]
        """
        violations = []
        if dependency_graph is None:
            return violations
        for dependency in dependency_graph.dependencies:
            violation = self._analyze_edge(dependency)
            if violation is not None:
                violations.append(violation)
        return violations

    def _analyze_edge(self, edge):
        """
        Analyze a single dependency edge.
        """

        source = edge.source
        target = edge.target

        source_layer = self._get_layer(source)
        target_layer = self._get_layer(target)

        if self.rule_service.is_allowed(
                source_layer,
                target_layer):
            return None

        severity = self.rule_service.violation_severity(
            source_layer,
            target_layer
        )

        description = self.rule_service.violation_description(
            source_layer,
            target_layer
        )

        return LayerViolation(
            source=source,
            target=target,
            source_layer=source_layer,
            target_layer=target_layer,
            rule_name="Layer Dependency Rule",
            severity=severity,
            description=description
        )

    def _get_layer(self, component):
        """
        Attempts to determine the layer for a component.

        Supported inputs:

        component.layer

        component.component_type

        component.type

        component.name

        string
        """

        if component is None:
            return "unknown"

        if hasattr(component, "layer"):
            layer = getattr(component, "layer")
            if layer:
                return str(layer).lower()

        if hasattr(component, "component_type"):
            layer = getattr(component, "component_type")
            if layer:
                return str(layer).lower()

        if hasattr(component, "type"):
            layer = getattr(component, "type")
            if layer:
                return str(layer).lower()

        if hasattr(component, "name"):
            return self._infer_layer_from_name(
                getattr(component, "name")
            )

        if isinstance(component, str):
            return self._infer_layer_from_name(component)

        return "unknown"

    def _infer_layer_from_name(self, name):
        """
        Infer architecture layer from naming conventions.
        """

        if name is None:
            return "unknown"

        value = str(name).lower()

        if "controller" in value:
            return "controller"

        if "service" in value:
            return "service"

        if "repository" in value:
            return "repository"

        if "dao" in value:
            return "repository"

        if "database" in value:
            return "database"

        if "entity" in value:
            return "entity"

        if "model" in value:
            return "model"

        if "view" in value:
            return "presentation"

        if "ui" in value:
            return "presentation"

        return "unknown"
