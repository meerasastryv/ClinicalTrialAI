"""
performance_dashboard.py

Displays a consolidated runtime performance dashboard.
"""


class PerformanceDashboard:
    """
    Displays runtime performance statistics.
    """

    def __init__(
        self,
        performance_repository=None,
        hotspot_repository=None,
        api_call_repository=None,
        database_query_repository=None,
        runtime_repository=None,
    ):
        self.performance_repository = performance_repository
        self.hotspot_repository = hotspot_repository
        self.api_call_repository = api_call_repository
        self.database_query_repository = database_query_repository
        self.runtime_repository = runtime_repository

    def display(self):

        print()
        print("=" * 70)
        print("RUNTIME PERFORMANCE DASHBOARD")
        print("=" * 70)

        runtime_events = (
            self.runtime_repository.size()
            if self.runtime_repository
            else 0
        )

        performance_metrics = (
            self.performance_repository.get_all_metrics()
            if self.performance_repository
            else []
        )

        hotspots = (
            self.hotspot_repository.get_all_hotspots()
            if self.hotspot_repository
            else []
        )

        api_calls = (
            self.api_call_repository.get_all_api_calls()
            if self.api_call_repository
            else []
        )

        database_queries = (
            self.database_query_repository.get_all_queries()
            if self.database_query_repository
            else []
        )

        print(f"Runtime Events        : {runtime_events}")
        print(f"Methods Profiled      : {len(performance_metrics)}")
        print(f"Performance Hotspots  : {len(hotspots)}")
        print(f"API Calls             : {len(api_calls)}")
        print(f"Database Queries      : {len(database_queries)}")

        print()

        if performance_metrics:

            slowest = max(
                performance_metrics,
                key=lambda m: m.maximum_time,
            )

            print(
                f"Slowest Method        : "
                f"{slowest.method_name}"
            )

            print(
                f"Maximum Time (ms)     : "
                f"{slowest.maximum_time:.3f}"
            )

            avg = (
                sum(
                    m.average_time
                    for m in performance_metrics
                )
                / len(performance_metrics)
            )

            print(
                f"Average Method Time   : "
                f"{avg:.3f} ms"
            )

        else:

            print("Slowest Method        : N/A")
            print("Maximum Time (ms)     : N/A")
            print("Average Method Time   : N/A")

        print("=" * 70)
        print()
