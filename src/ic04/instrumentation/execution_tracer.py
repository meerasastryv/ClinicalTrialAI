import functools
import time

from src.ic04.collectors.runtime_profiler import RuntimeProfiler
from src.ic04.instrumentation.execution_context import ExecutionContext
from src.ic04.services.runtime_analysis_service import RuntimeAnalysisService


runtime_service = RuntimeAnalysisService()


def trace_execution(func):
    """
    Decorator that automatically captures runtime execution events.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        module_name = func.__module__

        class_name = ""

        if args:
            class_name = args[0].__class__.__name__

        method_name = func.__name__

        ExecutionContext.push(method_name)

        runtime_service.record_event(
            RuntimeProfiler.create_event(
                event_type="METHOD_START",
                module_name=module_name,
                class_name=class_name,
                method_name=method_name,
                caller=ExecutionContext.caller(),
            )
        )

        start = time.perf_counter()

        try:

            result = func(*args, **kwargs)

        except Exception as ex:

            runtime_service.record_event(
                RuntimeProfiler.create_event(
                    event_type="METHOD_EXCEPTION",
                    module_name=module_name,
                    class_name=class_name,
                    method_name=method_name,
                    caller=ExecutionContext.caller(),
                    status="FAILED",
                    exception=str(ex),
                )
            )

            ExecutionContext.pop()

            raise

        duration = (time.perf_counter() - start) * 1000

        runtime_service.record_event(
            RuntimeProfiler.create_event(
                event_type="METHOD_END",
                module_name=module_name,
                class_name=class_name,
                method_name=method_name,
                caller=ExecutionContext.caller(),
                duration_ms=duration,
            )
        )

        ExecutionContext.pop()

        return result

    return wrapper
