class AICodeAssistantReport:
    """
    Demonstrates the AI Code Assistant capabilities.
    """

    def __init__(self, assistant):

        self.assistant = assistant

    def print_report(self):

        print("=" * 70)
        print("              AI CODE ASSISTANT REPORT")
        print("=" * 70)

        #
        # Platform Summary
        #
        print("\nPlatform Summary")
        print("-" * 70)

        summary = self.assistant.platform_summary()

        project = summary["project"]

        print(f"Nodes                  : {project['nodes']}")
        print(f"Relationships          : {project['relationships']}")
        print(f"Architecture Health    : {project['health_score']}%")
        print(f"Stability Index        : {project['stability_index']}%")

        #
        # Sample Questions
        #
        print("\nSample AI Questions")
        print("-" * 70)

        questions = [

            "Architecture summary",

            "Show health",

            "Show hotspots",

            "Show cycles",

            "Show coupling"

        ]

        for question in questions:

            print(f"\nQuestion : {question}")

            answer = self.assistant.answer(question)

            print(f"Answer   : {answer}")

        #
        # Component Explanation Demo
        #
        print("\nComponent Explanation")
        print("-" * 70)

        component = "ProjectAnalysisService"

        print(f"Component : {component}")

        print(self.assistant.explain_component(component))

        #
        # Impact Demo
        #
        print("\nImpact Analysis")
        print("-" * 70)

        print(self.assistant.explain_impact(component))

        #
        # Search Demo
        #
        print("\nSearch Example")
        print("-" * 70)

        results = self.assistant.search("Dependency")

        if not results:

            print("No matching components found.")

        else:

            for item in results[:10]:

                print(item)

        print("=" * 70)
