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

from src.ic05.query.graph_query_service import GraphQueryService
from src.ic05.query.graph_query_report import GraphQueryReport as QueryReport

from src.ic05.services.graph_query_engine import GraphQueryEngine
from src.ic05.reports.graph_query_report import GraphQueryReport


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

    #
    # ===============================================================
    # IC-05 Knowledge Graph Engine
    # ===============================================================
    #

    print()
    print("=" * 70)
    print("IC-05 Knowledge Graph Engine")
    print("=" * 70)

    graph_service = GraphService()

    #
    # Create Knowledge Graph Nodes
    #

    graph_service.add_node(
        node_id="REQ-001",
        node_type="Requirement",
        name="User Login",
    )

    graph_service.add_node(
        node_id="CLASS-001",
        node_type="Class",
        name="AuthenticationService",
    )

    graph_service.add_node(
        node_id="METHOD-001",
        node_type="Method",
        name="authenticate_user",
        properties={
            "requirement": "REQ-001",
            "class": "CLASS-001",
            "api": "API-001",
            "database": "DB-001",
        },
    )

    graph_service.add_node(
        node_id="API-001",
        node_type="API",
        name="/login",
    )

    graph_service.add_node(
        node_id="DB-001",
        node_type="Database",
        name="USER_TABLE",
    )

    graph_service.add_node(
        node_id="RT-001",
        node_type="Runtime",
        name="Authentication Runtime",
        properties={
            "runtime": "METHOD-001",
        },
    )

    #
    # Automatic Relationship Detection
    #

    summary = graph_service.detect_relationships()

    print()
    print("-" * 70)
    print("Relationship Detection")
    print("-" * 70)
    print(f"Relationships Detected : {summary['detected']}")
    print(f"Relationships Created  : {summary['created']}")

    #
    # Graph Report
    #

    graph_service.generate_report()

    #
    # Validation
    #

    validation = graph_service.validate_graph()

    print()
    print("=" * 70)
    print("GRAPH VALIDATION")
    print("=" * 70)

    for key, value in validation.items():
        print(f"{key:25}: {value}")

    #
    # ===============================================================
    # IC-05 Milestone 9 - Graph Query Engine
    # ===============================================================
    #

    query_service = GraphQueryService(graph_service.repository)

    print()
    print("=" * 70)
    print("GRAPH QUERY ENGINE")
    print("=" * 70)

    #
    # Neighbors
    #

    neighbors = query_service.neighbors("REQ-001")
    QueryReport.print_neighbors("REQ-001", neighbors)

    #
    # Shortest Path
    #

    path = query_service.path("REQ-001", "DB-001")
    QueryReport.print_path(path)

    #
    # Search by Type
    #

    requirement_nodes = query_service.search_type("Requirement")
    QueryReport.print_search(
        "REQUIREMENT NODES",
        requirement_nodes,
    )

    #
    # Search by Name
    #

    login_nodes = query_service.search_name("login")
    QueryReport.print_search(
        "SEARCH RESULTS : login",
        login_nodes,
    )

    #
    # Connected Nodes
    #

    connected = query_service.connected("REQ-001")
    QueryReport.print_connected(connected)
    print()
    print("=" * 70)
    print("IC-05 Milestone 10 - Graph Analytics")
    print("=" * 70)
    query_engine = GraphQueryEngine(graph_service.repository)
    stats = query_engine.graph_statistics()
    print(stats)
    report = GraphQueryReport(graph_service.repository)
    report_file = report.generate()
    print()
    print(f"Graph Query Report generated : {report_file}")
    #print()
    #print("CONNECTED COMPONENT")
    #print("=" * 70)
    #for node in sorted(connected ,key=lambda x: x.node_id):
    #    print(node)
    #for node in sorted(connected):
    #   QueryReport.print_connected(connected)
if __name__ == "__main__":
    main()
