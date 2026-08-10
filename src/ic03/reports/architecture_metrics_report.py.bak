class ArchitectureMetricsReport:
    """
    Prints architecture metrics.
    """

    def __init__(self, metrics_service):

        self.metrics = metrics_service

    def print_report(self):

        print("=" * 70)
        print("               ARCHITECTURE METRICS REPORT")
        print("=" * 70)

        summary = self.metrics.summary()

        print(f"Total Nodes          : {summary['nodes']}")
        print(f"Total Relationships  : {summary['edges']}")
        print(f"Average Fan-In       : {summary['average_fan_in']}")
        print(f"Average Fan-Out      : {summary['average_fan_out']}")
        print(f"Architecture Health  : {summary['health_score']}%")
        print(f"Architecture Hotspots: {summary['hotspots']}")

        #
        # Top Fan-Out
        #
        print("\nTop Fan-Out")
        print("-" * 70)

        for node, degree in self.metrics.top_fan_out():

            print(f"{node:<45} {degree:>5}")

        #
        # Top Fan-In
        #
        print("\nTop Fan-In")
        print("-" * 70)

        for node, degree in self.metrics.top_fan_in():

            print(f"{node:<45} {degree:>5}")

        #
        # Hotspots
        #
        print("\nArchitecture Hotspots")
        print("-" * 70)

        hotspots = self.metrics.hotspots()

        if not hotspots:

            print("No hotspots detected.")

        else:

            for node, fan_in, fan_out in hotspots:

                print(
                    f"{node:<45} "
                    f"Fan-In={fan_in:<3} "
                    f"Fan-Out={fan_out:<3}"
                )

        print("=" * 70)
