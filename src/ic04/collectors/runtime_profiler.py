from datetime import datetime
import threading

from src.ic04.models.runtime_event import RuntimeEvent
from src.ic04.tracing.trace_context import TraceContext


class RuntimeProfiler:
    """
    Creates runtime events for execution tracking.
    """

    @staticmethod
    def create_event(
        event_type: str,
        module_name: str,
        class_name: str,
        method_name: str,
        caller=None,
        status="SUCCESS",
        duration_ms=None,
        exception=None,
    ) -> RuntimeEvent:

        return RuntimeEvent(
            timestamp=datetime.now(),
            trace_id=TraceContext.current_trace(),
            thread_name=threading.current_thread().name,
            event_type=event_type,
            module_name=module_name,
            class_name=class_name,
            method_name=method_name,
            caller=caller,
            duration_ms=duration_ms,
            status=status,
            exception=exception,
        )
