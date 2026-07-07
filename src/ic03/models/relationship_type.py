from enum import Enum


class RelationshipType(Enum):
    """
    Types of relationships that can exist in the codebase.
    """

    IMPORTS = "IMPORTS"

    CALLS = "CALLS"

    INHERITS = "INHERITS"

    USES = "USES"

    REFERENCES = "REFERENCES"

    IMPLEMENTS = "IMPLEMENTS"
