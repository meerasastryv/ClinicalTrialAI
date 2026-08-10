"""
Layer Violation Model

Represents an architecture layer violation.
"""


class LayerViolation:
    """
    Represents a detected layer violation.
    """

    def __init__(
        self,
        source,
        target,
        source_layer,
        target_layer,
        rule_name,
        severity,
        description
    ):
        self.source = source
        self.target = target
        self.source_layer = source_layer
        self.target_layer = target_layer
        self.rule_name = rule_name
        self.severity = severity
        self.description = description

    def to_dict(self):
        """Convert object to dictionary."""

        return {
            "source": self.source,
            "target": self.target,
            "source_layer": self.source_layer,
            "target_layer": self.target_layer,
            "rule_name": self.rule_name,
            "severity": self.severity,
            "description": self.description
        }

    def __str__(self):
        return (
            f"{self.source} ({self.source_layer}) -> "
            f"{self.target} ({self.target_layer}) | "
            f"{self.severity}"
        )

    def __repr__(self):
        return self.__str__()
