from enum import Enum


class DependencyType(Enum):
    """
    Types of software dependencies.
    """

    IMPORT = "IMPORT"

    CLASS_DEPENDENCY = "CLASS_DEPENDENCY"

    METHOD_CALL = "METHOD_CALL"

    INHERITANCE = "INHERITANCE"

    ATTRIBUTE = "ATTRIBUTE"

    ANNOTATION = "ANNOTATION"
