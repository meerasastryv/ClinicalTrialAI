from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class RuntimeEvent:
    """
    Represents a generic runtime event captured during execution.
    """

    timestamp: datetime

    trace_id: Optional[str]

    thread_name: str

    event_type: str

    module_name: str

    class_name: str

    method_name: str

    caller: Optional[str] = None

    callee: Optional[str] = None

    duration_ms: Optional[float] = None

    status: str = "SUCCESS"

    exception: Optional[str] = None
