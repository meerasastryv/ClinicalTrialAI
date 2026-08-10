"""
runtime_visualizer.py

Central visualization service for Runtime Exploration.
"""

from src.ic04.visualization.performance_dashboard import (
    PerformanceDashboard,
)
from src.ic04.visualization.execution_graph import (
    ExecutionGraph,
)


class RuntimeVisualizer:
    """
    Provides a unified interface for visualizing all
    runtime exploration artifacts.
    """

    def __init__(
        self,
        runtime_repository=None,
        performance_repository=None,
        hotspot_repository=None,
        api_call_repository=None,
        database_query_repository=None,
        runtime_knowledge=None,
    ):
        self.runtime_repository = runtime_repository
        self.performance_repository = performance_repository
        self.hotspot_repository = hotspot_repository
        self.api_call_repository = api_call_repository
        self.database_query_repository = database_query_repository
        self.runtime_knowledge = runtime_knowledge

    def show_dashboard(self):

        dashboard = PerformanceDashboard(
            performance_repository=self.performance_repository,
            hotspot_repository=self.hotspot_repository,
            api_call_repository=self.api_call_repository,
            database_query_repository=self.database_query_repository,
            runtime_repository=self.runtime_repository,
        )

        dashboard.display()

    def show_execution_graph(self):

        graph = ExecutionGraph(
            self.runtime_repository.get_all_events()
            if self.runtime_repository
            else []
        )

        graph.display()

    def show_hotspots(self):

        print()
        print("=" * 70)
        print("PERFORMANCE HOTSPOTS")
        print("=" * 70)

        hotspots = (
            self.hotspot_repository.get_sorted_hotspots()
            if self.hotspot_repository
            else []
        )

        if not hotspots:
            print("No hotspots available.")
        else:

            print(
                f"{'Method':35}"
                f"{'Average(ms)':>15}"
                f"{'Level':>15}"
            )
            print("-" * 70)

            for hotspot in hotspots:
                print(
                    f"{hotspot.method_name:35}"
                    f"{hotspot.average_time:15.3f}"
                    f"{hotspot.hotspot_level:>15}"
                )

        print("=" * 70)
        print()

    def show_api_calls(self):

        print()
        print("=" * 70)
        print("API CALLS")
        print("=" * 70)

        calls = (
            self.api_call_repository.get_all_api_calls()
            if self.api_call_repository
            else []
        )

        if not calls:
            print("No API calls recorded.")
        else:
            for call in calls:
                print(
                    f"{call.http_method:6}"
                    f"{call.endpoint:25}"
                    f"{call.duration_ms:10.2f} ms"
                )

        print("=" * 70)
        print()

    def show_database_queries(self):

        print()
        print("=" * 70)
        print("DATABASE QUERIES")
        print("=" * 70)

        queries = (
            self.database_query_repository.get_all_queries()
            if self.database_query_repository
            else []
        )

        if not queries:
            print("No database queries recorded.")
        else:
            for query in queries:
                print(
                    f"{query.operation:8}"
                    f"{query.table_name:20}"
                    f"{query.duration_ms:10.2f} ms"
                )

        print("=" * 70)
        print()

    def show_runtime_knowledge(self):

        print()
        print("=" * 70)
        print("RUNTIME KNOWLEDGE")
        print("=" * 70)

        if self.runtime_knowledge is None:
            print("No runtime knowledge available.")
        else:
            summary = self.runtime_knowledge.execution_summary

            for key, value in summary.items():
                print(f"{key:30}: {value}")

        print("=" * 70)
        print()

    def show_all(self):

        self.show_dashboard()
        self.show_execution_graph()
        self.show_hotspots()
        self.show_api_calls()
        self.show_database_queries()
        self.show_runtime_knowledge()
