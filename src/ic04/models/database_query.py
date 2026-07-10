from dataclasses import dataclass


@dataclass
class DatabaseQuery:
    """
    Represents a database query executed at runtime.
    """

    query: str

    database: str

    duration_ms: float

    success: bool
