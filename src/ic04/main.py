from src.ic04.builders.runtime_graph_builder import RuntimeGraphBuilder
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

    print(f"Runtime Events: {runtime_service.get_event_count()}")

    graph_builder = RuntimeGraphBuilder()

    graph = graph_builder.build(
        runtime_service.get_runtime_events()
    )

    print()

    print(f"Runtime Relationships: {graph.size()}")

    print()

    for relationship in graph.get_relationships():

        print(
            f"{relationship.caller}"
            f" --> "
            f"{relationship.callee}"
            f" | calls={relationship.call_count}"
            f" | duration={relationship.total_duration_ms:.3f} ms"
        )


if __name__ == "__main__":
    main()
