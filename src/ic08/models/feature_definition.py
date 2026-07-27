"""
feature_definition.py

Model describing a machine learning feature used by
Customer Usage Intelligence.
"""

from dataclasses import dataclass


@dataclass
class FeatureDefinition:
    """
    Defines one feature used in machine learning.
    """

    name: str

    description: str

    source: str

    data_type: str = "float"

    normalized: bool = False

    enabled: bool = True

    def __str__(self) -> str:
        return (
            f"FeatureDefinition("
            f"name={self.name}, "
            f"source={self.source}, "
            f"normalized={self.normalized})"
        )
