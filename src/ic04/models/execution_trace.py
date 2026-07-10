from dataclasses import dataclass, field
from typing import List

from .runtime_event import RuntimeEvent


@dataclass
class ExecutionTrace:
    """
    Represents a complete execution trace.
    """

    trace_id: str

    events: List[RuntimeEvent] = field(default_factory=list)
