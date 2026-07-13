from src.ic04.analyzers.hotspot_analyzer import HotspotAnalyzer
from src.ic04.analyzers.performance_analyzer import PerformanceAnalyzer
from src.ic04.builders.runtime_graph_builder import RuntimeGraphBuilder
from src.ic04.collectors.api_call_collector import ApiCallCollector
from src.ic04.collectors.database_query_collector import DatabaseQueryCollector
from src.ic04.instrumentation.execution_tracer import (
    runtime_service,
    trace_execution,
)
from src.ic04.repositories.runtime_knowledge_repository import (
    RuntimeKnowledgeRepository,
)
from src.ic04.reports.api_call_report import ApiCallReport
from src.ic04.reports.database_query_report import DatabaseQueryReport
from src.ic04.reports.hotspot_report import HotspotReport
from src.ic04.reports.performance_report import PerformanceReport
from src.ic04.reports.runtime_knowledge_report import (
    RuntimeKnowledgeReport,
)
from src.ic04.cli.runtime_cli import RuntimeCLI

from src.ic05.services.graph_service import GraphService
from src.ic05.reports.graph_report import GraphReport


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

    graph_builder = RuntimeGraphBuilder()
    graph = graph_builder.build(runtime_service.get_runtime_events())

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

    print()
    print("=" * 70)
    print("PERFORMANCE ANALYSIS")
    print("=" * 70)

    performance_repository = PerformanceAnalyzer().analyze(
        runtime_service.get_repository()
    )
    PerformanceReport(performance_repository).print_report()

    print()
    print("=" * 70)
    print("HOTSPOT ANALYSIS")
    print("=" * 70)

    hotspot_repository = HotspotAnalyzer().analyze(
        performance_repository
    )
    HotspotReport(hotspot_repository).print_report()

    print()
    print("=" * 70)
    print("API CALL ANALYSIS")
    print("=" * 70)

    ApiCallReport(
        api_collector.get_repository()
    ).print_report()

    print()
    print("=" * 70)
    print("DATABASE QUERY ANALYSIS")
    print("=" * 70)

    DatabaseQueryReport(
        database_collector.get_repository()
    ).print_report()

    knowledge = RuntimeKnowledgeRepository().build(
        runtime_repository=runtime_service.get_repository(),
        performance_repository=performance_repository,
        hotspot_repository=hotspot_repository,
        api_call_repository=api_collector.get_repository(),
        database_query_repository=database_collector.get_repository(),
    )

    RuntimeKnowledgeReport.print_report(knowledge)

    print()
    print("=" * 70)
    print("RUNTIME EXPLORER")
    print("=" * 70)

    runtime_cli = RuntimeCLI(
        runtime_repository=runtime_service.get_repository(),
        performance_repository=performance_repository,
        hotspot_repository=hotspot_repository,
        api_call_repository=api_collector.get_repository(),
        database_query_repository=database_collector.get_repository(),
        runtime_knowledge=knowledge,
    )

    runtime_cli.run()

    print()
    print("=" * 70)
    print("IC-05 Knowledge Graph Engine")
    print("=" * 70)

    graph_service = GraphService()

    graph_service.add_node(
        node_id="REQ-001",
        node_type="Requirement",
        name="User Login",
    )

    graph_service.add_node(
        node_id="METHOD-001",
        node_type="Method",
        name="authenticate_user",
    )

    graph_service.add_node(
        node_id="API-001",
        node_type="API",
        name="/login",
    )

    graph_service.add_edge(
        source="METHOD-001",
        target="REQ-001",
        relationship="IMPLEMENTS",
    )

    graph_service.add_edge(
        source="METHOD-001",
        target="API-001",
        relationship="CALLS",
    )

    GraphReport(graph_service).print_report()


if __name__ == "__main__":
    main()
