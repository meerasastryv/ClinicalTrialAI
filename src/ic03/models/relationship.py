from dataclasses import dataclass


@dataclass
class Relationship:
    """
    Represents a relationship discovered in the source code.
    """

    source: str
    relationship_type: str
    target: str
