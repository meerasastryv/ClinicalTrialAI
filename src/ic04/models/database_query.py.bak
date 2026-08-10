"""
database_query.py

Represents a database query captured during runtime.
"""

from dataclasses import dataclass


@dataclass
class DatabaseQuery:
    """
    Represents a single database query execution.
    """

    operation: str

    table_name: str

    caller_method: str

    duration_ms: float

    rows_affected: int = 0

    def to_dict(self):
        """
        Convert query to dictionary representation.
        """
        return {
            "operation": self.operation,
            "table_name": self.table_name,
            "caller_method": self.caller_method,
            "duration_ms": round(self.duration_ms, 6),
            "rows_affected": self.rows_affected,
        }

    def __str__(self):
        return (
            f"{self.operation} "
            f"{self.table_name} | "
            f"Caller={self.caller_method} | "
            f"Duration={self.duration_ms:.3f} ms | "
            f"Rows={self.rows_affected}"
        )
