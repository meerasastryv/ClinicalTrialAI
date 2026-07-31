"""
metrics.py

Reusable metrics collector.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Metrics:

    values: Dict[str, float] = field(default_factory=dict)

    def increment(self, name: str, amount: float = 1):

        self.values[name] = self.values.get(name, 0) + amount

    def set(self, name: str, value: float):

        self.values[name] = value

    def get(self, name: str):

        return self.values.get(name, 0)

    def as_dict(self):

        return dict(self.values)
