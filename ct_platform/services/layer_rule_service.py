"""
Layer Rule Service

Defines the allowed architecture layer transitions and provides
helper methods to validate dependencies.
"""


class LayerRuleService:
    """
    Central rule engine for architecture layer validation.
    """

    # Lower value = Higher layer
    LAYER_ORDER = {
        "presentation": 1,
        "controller": 1,

        "business": 2,
        "service": 2,

        "repository": 3,
        "data": 3,

        "database": 4,

        "entity": 5,
        "model": 5,

        "unknown": 999
    }

    ALLOWED_DEPENDENCIES = {

        "presentation": [
            "business",
            "service",
            "controller"
        ],

        "controller": [
            "service",
            "business"
        ],

        "business": [
            "repository",
            "service"
        ],

        "service": [
            "repository",
            "service"
        ],

        "repository": [
            "database",
            "repository"
        ],

        "database": [],

        "entity": [],

        "model": []
    }

    def get_layer_order(self, layer):
        """
        Returns numeric order of a layer.
        """

        if layer is None:
            return 999

        return self.LAYER_ORDER.get(
            layer.lower(),
            999
        )

    def is_allowed(
            self,
            source_layer,
            target_layer):
        """
        Checks whether dependency is allowed.
        """

        if source_layer is None or target_layer is None:
            return False

        allowed = self.ALLOWED_DEPENDENCIES.get(
            source_layer.lower(),
            []
        )

        return target_layer.lower() in allowed

    def is_upward_dependency(
            self,
            source_layer,
            target_layer):
        """
        Repository -> Controller
        Service -> Controller

        are upward dependencies.
        """

        return (
            self.get_layer_order(target_layer)
            <
            self.get_layer_order(source_layer)
        )

    def is_same_layer(
            self,
            source_layer,
            target_layer):
        """
        Checks whether dependency exists within
        same architecture layer.
        """

        return (
            self.get_layer_order(source_layer)
            ==
            self.get_layer_order(target_layer)
        )

    def skipped_layer(
            self,
            source_layer,
            target_layer):
        """
        Detects layer skipping.

        Example:

        Controller -> Repository
        """

        source = self.get_layer_order(source_layer)
        target = self.get_layer_order(target_layer)

        return (target - source) > 1

    def violation_severity(
            self,
            source_layer,
            target_layer):
        """
        Determines severity.
        """

        if self.is_upward_dependency(
                source_layer,
                target_layer):
            return "CRITICAL"

        if self.skipped_layer(
                source_layer,
                target_layer):
            return "HIGH"

        return "MEDIUM"

    def violation_description(
            self,
            source_layer,
            target_layer):
        """
        Creates a readable violation message.
        """

        return (
            f"Dependency from "
            f"{source_layer} "
            f"to "
            f"{target_layer} "
            f"is not permitted."
        )
