from src.ic04.models.runtime_knowledge import RuntimeKnowledge


class RuntimeKnowledgeRepository:
    """
    Consolidates all runtime repositories into a single
    RuntimeKnowledge object.
    """

    def build(
        self,
        runtime_repository=None,
        performance_repository=None,
        hotspot_repository=None,
        api_call_repository=None,
        database_query_repository=None,
    ) -> RuntimeKnowledge:
        """
        Build and return a consolidated RuntimeKnowledge object.
        """

        knowledge = RuntimeKnowledge()

        # Store repository references
        knowledge.runtime_repository = runtime_repository
        knowledge.performance_repository = performance_repository
        knowledge.hotspot_repository = hotspot_repository
        knowledge.api_call_repository = api_call_repository
        knowledge.database_query_repository = (
            database_query_repository
        )

        # Runtime Event Count
        runtime_events = (
            runtime_repository.size()
            if runtime_repository is not None
            else 0
        )

        # Performance Metrics Count
        performance_metrics = (
            len(performance_repository.get_all_metrics())
            if performance_repository is not None
            else 0
        )

        # Hotspot Count
        hotspots = (
            len(hotspot_repository.get_all_hotspots())
            if hotspot_repository is not None
            else 0
        )

        # API Call Count
        api_calls = (
            len(api_call_repository.get_all_api_calls())
            if api_call_repository is not None
            else 0
        )

        # Database Query Count
        database_queries = (
            len(database_query_repository.get_all_queries())
            if database_query_repository is not None
            else 0
        )

        # Execution Summary
        knowledge.execution_summary = {
            "runtime_events": runtime_events,
            "performance_metrics": performance_metrics,
            "hotspots": hotspots,
            "api_calls": api_calls,
            "database_queries": database_queries,
            "total_runtime_artifacts": (
                runtime_events
                + performance_metrics
                + hotspots
                + api_calls
                + database_queries
            ),
        }

        return knowledge
