from src.ic04.analyzers.hotspot_analyzer import HotspotAnalyzer
from src.ic04.analyzers.performance_analyzer import PerformanceAnalyzer
from src.ic04.builders.runtime_graph_builder import RuntimeGraphBuilder
from src.ic04.instrumentation.execution_tracer import (
    runtime_service,
    trace_execution,
)
from src.ic04.reports.hotspot_report import HotspotReport
from src.ic04.reports.performance_report import PerformanceReport


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

    print(f"Runtime Events : {runtime_service.get_event_count()}")

    # ---------------------------------------------------------
    # Build Runtime Graph
    # ---------------------------------------------------------

    graph_builder = RuntimeGraphBuilder()

    graph = graph_builder.build(
        runtime_service.get_runtime_events()
    )

    print(f"Relationships : {graph.size()}")

    print()

    print("Runtime Events")

    print("-" * 70)

    for event in runtime_service.get_runtime_events():

        print(
            f"{event.trace_id:15}"
            f"{event.event_type:18}"
            f"{event.method_name:20}"
            f"caller={event.caller}"
        )

    print()

    print("Runtime Graph")

    print("-" * 70)

    for relationship in graph.get_relationships():

        print(
            f"{relationship.caller}"
            f" --> "
            f"{relationship.callee}"
            f" | calls={relationship.call_count}"
            f" | duration={relationship.total_duration_ms:.3f} ms"
        )

    # ---------------------------------------------------------
    # Performance Analysis (Milestone 7)
    # ---------------------------------------------------------

    print()
    print("=" * 70)
    print("PERFORMANCE ANALYSIS")
    print("=" * 70)

    performance_analyzer = PerformanceAnalyzer()

    performance_repository = performance_analyzer.analyze(
        runtime_service.get_repository()
    )

    performance_report = PerformanceReport(
        performance_repository
    )

    print()

    performance_report.print_report()

    # ---------------------------------------------------------
    # Hotspot Analysis (Milestone 8)
    # ---------------------------------------------------------

    print()
    print("=" * 70)
    print("HOTSPOT ANALYSIS")
    print("=" * 70)

    hotspot_analyzer = HotspotAnalyzer()

    hotspot_repository = hotspot_analyzer.analyze(
        performance_repository
    )

    hotspot_report = HotspotReport(
        hotspot_repository
    )

    print()

    hotspot_report.print_report()


if __name__ == "__main__":
    main()
