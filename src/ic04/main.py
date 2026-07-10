from src.ic04.collectors.runtime_profiler import RuntimeProfiler
from src.ic04.services.runtime_analysis_service import RuntimeAnalysisService


def main():

    service = RuntimeAnalysisService()

    event1 = RuntimeProfiler.create_event(
        event_type="METHOD_START",
        module_name="sample",
        class_name="Demo",
        method_name="run",
    )

    event2 = RuntimeProfiler.create_event(
        event_type="METHOD_END",
        module_name="sample",
        class_name="Demo",
        method_name="run",
        duration_ms=12.8,
    )

    service.record_event(event1)
    service.record_event(event2)

    print("=" * 60)
    print("IC-04 Runtime Exploration Agent")
    print("=" * 60)

    print()

    print(f"Total Runtime Events: {service.get_event_count()}")

    print()

    for event in service.get_runtime_events():
        print(event)


if __name__ == "__main__":
    main()
