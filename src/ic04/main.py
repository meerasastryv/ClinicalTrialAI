from src.ic04.instrumentation.execution_tracer import (
    trace_execution,
    runtime_service,
)


class DemoApplication:

    @trace_execution
    def calculate(self):
        return self.compute_total()

    @trace_execution
    def compute_total(self):

        self.validate()

        total = 0

        for i in range(50000):
            total += i

        return total

    @trace_execution
    def validate(self):
        return True


def main():

    app = DemoApplication()

    app.calculate()

    print("=" * 70)
    print("IC-04 Runtime Exploration Agent")
    print("=" * 70)

    print()

    print(f"Total Runtime Events: {runtime_service.get_event_count()}")

    print()

    for event in runtime_service.get_runtime_events():
        print(event)


if __name__ == "__main__":
    main()
