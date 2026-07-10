from datetime import datetime

from src.ic04.models.runtime_event import RuntimeEvent


def main():

    event = RuntimeEvent(
        timestamp=datetime.now(),
        thread_name="MainThread",
        event_type="METHOD_START",
        module_name="sample",
        class_name="Demo",
        method_name="run"
    )

    print("=" * 60)
    print("IC-04 Runtime Exploration Agent")
    print("=" * 60)
    print()

    print("Runtime Event Created Successfully")
    print()

    print(event)


if __name__ == "__main__":
    main()
