from src.ic04.models.runtime_knowledge import RuntimeKnowledge


class RuntimeKnowledgeReport:
    """
    Prints the consolidated Runtime Knowledge Repository.
    """

    @staticmethod
    def print_report(knowledge: RuntimeKnowledge):

        print()
        print("=" * 70)
        print("RUNTIME KNOWLEDGE REPOSITORY")
        print("=" * 70)

        summary = knowledge.execution_summary

        print(
            f"Runtime Events        : "
            f"{summary.get('runtime_events', 0)}"
        )

        print(
            f"Performance Metrics   : "
            f"{summary.get('performance_metrics', 0)}"
        )

        print(
            f"Hotspots              : "
            f"{summary.get('hotspots', 0)}"
        )

        print(
            f"API Calls             : "
            f"{summary.get('api_calls', 0)}"
        )

        print(
            f"Database Queries      : "
            f"{summary.get('database_queries', 0)}"
        )

        print("-" * 70)

        print(
            f"Total Runtime Artifacts : "
            f"{summary.get('total_runtime_artifacts', 0)}"
        )

        print("=" * 70)
