import threading
import uuid


class TraceContext:
    """
    Maintains the current execution trace.
    """

    _local = threading.local()

    @classmethod
    def begin_trace(cls):

        trace_id = str(uuid.uuid4())[:8]

        cls._local.trace_id = f"TRACE-{trace_id}"

        return cls._local.trace_id

    @classmethod
    def current_trace(cls):

        return getattr(cls._local, "trace_id", None)

    @classmethod
    def end_trace(cls):

        if hasattr(cls._local, "trace_id"):
            del cls._local.trace_id
