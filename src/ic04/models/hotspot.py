"""
hotspot.py

Represents a runtime performance hotspot.
"""

from dataclasses import dataclass


@dataclass
class Hotspot:
    """
    Represents a runtime hotspot for a method.
    """

    method_name: str

    call_count: int

    average_time: float

    total_time: float

    hotspot_level: str

    def to_dict(self):
        """
        Convert hotspot to dictionary representation.
        """
        return {
            "method_name": self.method_name,
            "call_count": self.call_count,
            "average_time": round(self.average_time, 6),
            "total_time": round(self.total_time, 6),
            "hotspot_level": self.hotspot_level,
        }

    def __str__(self):
        return (
            f"{self.method_name} | "
            f"Calls={self.call_count} | "
            f"Avg={self.average_time:.6f} ms | "
            f"Total={self.total_time:.6f} ms | "
            f"Level={self.hotspot_level}"
        )
