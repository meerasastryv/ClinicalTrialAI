from src.ic04.analyzers.hotspot_analyzer import HotspotAnalyzer
from src.ic04.analyzers.performance_analyzer import PerformanceAnalyzer
from src.ic04.builders.runtime_graph_builder import RuntimeGraphBuilder
from src.ic04.collectors.api_call_collector import ApiCallCollector
from src.ic04.collectors.database_query_collector import DatabaseQueryCollector
from src.ic04.instrumentation.execution_tracer import (
    runtime_service,
    trace_execution,
)
from src.ic04.reports.api_call_report import ApiCallReport
from src.ic04.reports.database_query_report import DatabaseQueryReport
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

    # ---------------------------------------------------------
    # Simulated API Calls (Milestone 9)
    # ---------------------------------------------------------

    api_collector = ApiCallCollector()

    api_collector.collect(
        endpoint="/patients",
        http_method="GET",
        caller_method="calculate",
        duration_ms=12.8,
    )

    api_collector.collect(
        endpoint="/studies",
        http_method="GET",
        caller_method="compute_total",
        duration_ms=18.3,
    )

    api_collector.collect(
        endpoint="/login",
        http_method="POST",
        caller_method="validate",
        duration_ms=7.5,
    )

    # ---------------------------------------------------------
    # Simulated Database Queries (Milestone 10)
    # ---------------------------------------------------------

    database_collector = DatabaseQueryCollector()

    database_collector.collect(
        operation="SELECT",
        table_name="PATIENT",
        caller_method="calculate",
        duration_ms=14.2,
        rows_affected=25,
    )

    database_collector.collect(
        operation="UPDATE",
        table_name="STUDY",
        caller_method="compute_total",
        duration_ms=21.6,
        rows_affected=2,
    )

    database_collector.collect(
        operation="INSERT",
        table_name="AUDIT_LOG",
        caller_method="validate",
        duration_ms=8.4,
        rows_affected=1,
    )

    print("=" * 70)
    print("IC-04 Runtime Exploration Agent")
    print("=" * 70)

    print()

    print(f"Runtime Events : {runtime_service.get_event_count()}")

    # ---------------------------------------------------------
    # Runtime Graph
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

    # ---------------------------------------------------------
    # API Call Analysis (Milestone 9)
    # ---------------------------------------------------------

    print()
    print("=" * 70)
    print("API CALL ANALYSIS")
    print("=" * 70)

    api_report = ApiCallReport(
        api_collector.get_repository()
    )

    print()

    api_report.print_report()

    # ---------------------------------------------------------
    # Database Query Analysis (Milestone 10)
    # ---------------------------------------------------------

    print()
    print("=" * 70)
    print("DATABASE QUERY ANALYSIS")
    print("=" * 70)

    database_report = DatabaseQueryReport(
        database_collector.get_repository()
    )

    print()

    database_report.print_report()


if __name__ == "__main__":
    main()
