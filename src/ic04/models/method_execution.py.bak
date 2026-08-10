from dataclasses import dataclass
from typing import Optional


@dataclass
class MethodExecution:
    """
    Represents execution statistics of a method.
    """

    module_name: str
    class_name: str
    method_name: str

    execution_count: int = 0

    total_duration_ms: float = 0.0

    min_duration_ms: Optional[float] = None

    max_duration_ms: Optional[float] = None
