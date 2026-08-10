class ImpactAnalysisReport:
    """
    Prints the results of the Impact Analysis Engine.
    """

    def __init__(self, impact_service):
        self.impact_service = impact_service

    def print_report(self):
        print()
        print("=" * 70)
        print("                 IMPACT ANALYSIS REPORT")
        print("=" * 70)

        summary = self.impact_service.impact_summary()

        print()
        print("Summary")
        print("-" * 70)
        print(f"Total Nodes            : {summary['total_nodes']}")
        print(
            f"Average Impact Score   : "
            f"{summary['average_impact_score']}"
        )
        print(
            f"Highest Impact Score   : "
            f"{summary['highest_impact_score']}"
        )
        print(
            f"Critical Nodes         : "
            f"{summary['critical_nodes']}"
        )

        print()
        print("Top High Impact Nodes")
        print("-" * 70)

        top_nodes = self.impact_service.high_impact_nodes(10)

        if not top_nodes:
            print("No impact information available.")
        else:
            for item in top_nodes:
                print(
                    f"{item['node']:<55}"
                    f"{item['impact_score']:>5}"
                )

        print()

        nodes = self.impact_service.traversal_service.get_nodes()

        if nodes:

            sample = nodes[0]

            print("Sample Impact Analysis")
            print("-" * 70)
            print(f"Node                : {sample}")

            affected = self.impact_service.affected_nodes(sample)

            print(f"Impact Score        : {self.impact_service.impact_score(sample)}")
            print(f"Dependency Depth    : {self.impact_service.dependency_depth(sample)}")
            print(f"Affected Nodes      : {len(affected)}")

            if affected:
                print()
                print("First 15 Affected Nodes")

                for node in affected[:15]:
                    print(f"  {node}")

                if len(affected) > 15:
                    print(f"  ... ({len(affected)} nodes)")

        print()
        print("=" * 70)
