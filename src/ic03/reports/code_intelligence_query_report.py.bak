class CodeIntelligenceQueryReport:
    """
    Prints a consolidated Code Intelligence report.
    """

    def __init__(self, query_service):

        self.query = query_service

    def print_report(self):

        print("=" * 70)
        print("           CODE INTELLIGENCE QUERY REPORT")
        print("=" * 70)

        #
        # Platform Summary
        #
        summary = self.query.summary()

        print("\nPlatform Summary")
        print("-" * 70)

        print(f"Nodes                  : {summary['project']['nodes']}")
        print(f"Relationships          : {summary['project']['relationships']}")
        print(f"Architecture Health    : {summary['project']['health_score']}%")
        print(f"Stability Index        : {summary['project']['stability_index']}%")
        print(f"Architecture Hotspots  : {summary['hotspots']}")
        print(f"Circular Dependencies  : {summary['cycles']}")
        print(f"Highly Coupled         : {summary['coupled_components']}")
        print(f"Orphan Components      : {summary['orphan_components']}")

        #
        # Top Architecture Hotspots
        #
        print("\nTop Architecture Hotspots")
        print("-" * 70)

        hotspots = self.query.architecture_hotspots()

        if not hotspots:

            print("None")

        else:

            for node, fan_in, fan_out in hotspots[:10]:

                print(
                    f"{node:<45}"
                    f"In={fan_in:<3}"
                    f" Out={fan_out:<3}"
                )

        #
        # Highly Coupled Components
        #
        print("\nHighly Coupled Components")
        print("-" * 70)

        coupled = self.query.highly_coupled_components()

        if not coupled:

            print("None")

        else:

            for node, fan_in, fan_out, total in coupled[:10]:

                print(
                    f"{node:<45}"
                    f"Total={total}"
                )

        #
        # Longest Dependency Chain
        #
        print("\nLongest Dependency Chain")
        print("-" * 70)

        chain = self.query.longest_dependency_chain()

        if not chain:

            print("None")

        else:

            print(" -> ".join(chain))

        #
        # Circular Dependencies
        #
        print("\nCircular Dependencies")
        print("-" * 70)

        cycles = self.query.circular_dependencies()

        if not cycles:

            print("None")

        else:

            for cycle in cycles[:10]:

                print(" -> ".join(cycle))

        print("=" * 70)
