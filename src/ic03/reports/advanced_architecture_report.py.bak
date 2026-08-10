class AdvancedArchitectureReport:
    """
    Prints advanced architecture analysis results.
    """

    def __init__(self, analysis_service):

        self.analysis = analysis_service

    def print_report(self):

        summary = self.analysis.detailed_summary()

        print("=" * 70)
        print("        ADVANCED ARCHITECTURE ANALYSIS REPORT")
        print("=" * 70)

        print(f"Components             : {summary['components']}")
        print(f"Relationships          : {summary['relationships']}")
        print(f"Orphan Components      : {summary['orphans']}")
        print(f"Highly Coupled         : {summary['highly_coupled']}")
        print(f"Circular Dependencies  : {summary['cycles']}")
        print(f"Maximum Chain Depth    : {summary['deepest_chain']}")
        print(f"Hub Components         : {summary['hub_components']}")
        print(f"Architecture Smells    : {summary['architecture_smells']}")
        print(f"Stability Index        : {summary['stability_index']}%")

        #
        # Highly Coupled Components
        #
        print("\nHighly Coupled Components")
        print("-" * 70)

        coupled = self.analysis.highly_coupled_components()

        if not coupled:

            print("None")

        else:

            for node, fan_in, fan_out, total in coupled:

                print(
                    f"{node:<45}"
                    f"In={fan_in:<3}"
                    f" Out={fan_out:<3}"
                    f" Total={total}"
                )

        #
        # Hub Components
        #
        print("\nHub Components")
        print("-" * 70)

        hubs = self.analysis.hub_components()

        if not hubs:

            print("None")

        else:

            for node, fan_in, fan_out in hubs:

                print(
                    f"{node:<45}"
                    f"In={fan_in:<3}"
                    f" Out={fan_out:<3}"
                )

        #
        # Circular Dependencies
        #
        print("\nCircular Dependencies")
        print("-" * 70)

        cycles = self.analysis.detect_cycles()

        if not cycles:

            print("No circular dependencies detected.")

        else:

            for cycle in cycles:

                print(" -> ".join(cycle))

        #
        # Longest Dependency Chain
        #
        print("\nLongest Dependency Chain")
        print("-" * 70)

        chain = self.analysis.longest_dependency_chain()

        if not chain:

            print("No dependency chains found.")

        else:

            print(" -> ".join(chain))

        #
        # Orphan Components
        #
        print("\nOrphan Components")
        print("-" * 70)

        orphans = self.analysis.orphan_components()

        if not orphans:

            print("None")

        else:

            for node in orphans:

                print(node)

        #
        # Architecture Smells
        #
        print("\nArchitecture Smells")
        print("-" * 70)

        smells = self.analysis.architecture_smells()

        if not smells:

            print("No architecture smells detected.")

        else:

            for smell, component in smells:

                print(f"{smell:<25} {component}")

        print("=" * 70)
