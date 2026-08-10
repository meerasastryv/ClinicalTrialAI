"""
runtime_cli.py

Interactive command-line interface for Runtime Exploration.
"""

from src.ic04.visualization.runtime_visualizer import (
    RuntimeVisualizer,
)


class RuntimeCLI:
    """
    Interactive CLI for exploring runtime artifacts.
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

        self.visualizer = RuntimeVisualizer(
            runtime_repository=runtime_repository,
            performance_repository=performance_repository,
            hotspot_repository=hotspot_repository,
            api_call_repository=api_call_repository,
            database_query_repository=database_query_repository,
            runtime_knowledge=runtime_knowledge,
        )

    def run(self):

        while True:

            print()
            print("=" * 70)
            print("ClinicalTrialAI Runtime Explorer")
            print("=" * 70)
            print("1. Runtime Dashboard")
            print("2. Execution Graph")
            print("3. Performance Hotspots")
            print("4. API Calls")
            print("5. Database Queries")
            print("6. Runtime Knowledge")
            print("7. Show Everything")
            print("0. Exit")
            print("=" * 70)

            choice = input("Select an option: ").strip()

            if choice == "1":
                self.visualizer.show_dashboard()

            elif choice == "2":
                self.visualizer.show_execution_graph()

            elif choice == "3":
                self.visualizer.show_hotspots()

            elif choice == "4":
                self.visualizer.show_api_calls()

            elif choice == "5":
                self.visualizer.show_database_queries()

            elif choice == "6":
                self.visualizer.show_runtime_knowledge()

            elif choice == "7":
                self.visualizer.show_all()

            elif choice == "0":
                print("\nExiting Runtime Explorer...\n")
                break

            else:
                print("\nInvalid selection. Please try again.\n")
