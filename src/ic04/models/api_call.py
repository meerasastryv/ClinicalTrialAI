"""
api_call.py

Represents an API call captured during runtime.
"""

from dataclasses import dataclass


@dataclass
class ApiCall:
    """
    Represents a single API invocation.
    """

    endpoint: str

    http_method: str

    caller_method: str

    duration_ms: float

    status_code: int = 200

    def to_dict(self):
        """
        Convert API call to dictionary representation.
        """
        return {
            "endpoint": self.endpoint,
            "http_method": self.http_method,
            "caller_method": self.caller_method,
            "duration_ms": round(self.duration_ms, 6),
            "status_code": self.status_code,
        }

    def __str__(self):
        return (
            f"{self.http_method} "
            f"{self.endpoint} | "
            f"Caller={self.caller_method} | "
            f"Duration={self.duration_ms:.3f} ms | "
            f"Status={self.status_code}"
        )
