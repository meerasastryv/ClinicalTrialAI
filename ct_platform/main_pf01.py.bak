"""
main_pf01.py

Platform Foundation Regression Suite

This program validates the Platform Foundation by executing
all available PF-01 analyzers and reporters.

Author: ClinicalTrialAI
"""

from pathlib import Path

from ct_platform.models.dependency import Dependency
from ct_platform.models.dependency_graph import DependencyGraph

from ct_platform.analyzers.architecture_analyzer import (
    ArchitectureAnalyzer,
)

from ct_platform.reporters.architecture_reporter import (
    ArchitectureReporter,
)


class PF01RegressionSuite:
    """
    Platform Foundation regression suite.
    """

    def __init__(self):

        self.report_directory = Path("reports")

        self.report_directory.mkdir(
            parents=True,
            exist_ok=True,
        )
        self.analyzer = ArchitectureAnalyzer()

        self.reporter = ArchitectureReporter(
            output_dir=self.report_directory
        )

        self.tests_passed = 0

        self.tests_failed = 0

    # ---------------------------------------------------------

    def banner(self):

        print()

        print("=" * 70)

        print("ClinicalTrialAI")

        print("Platform Foundation Regression Suite")

        print("=" * 70)

        print()

    # ---------------------------------------------------------

    def create_sample_graph(self):
        """
        Creates a sample dependency graph.
        """

        print(
            "Creating sample dependency graph..."
        )

        graph = DependencyGraph(
            engine_id="PF01-DEMO"
        )

        #
        # Sample layered architecture
        #

        graph.dependencies.extend(

            [

                Dependency(
                    source="controller.user_controller",
                    target="service.user_service",
                    dependency_type="import",
                ),

                Dependency(
                    source="service.user_service",
                    target="repository.user_repository",
                    dependency_type="import",
                ),

                Dependency(
                    source="repository.user_repository",
                    target="database.connection",
                    dependency_type="import",
                ),

                Dependency(
                    source="service.user_service",
                    target="utils.validator",
                    dependency_type="import",
                ),

                Dependency(
                    source="service.user_service",
                    target="utils.logger",
                    dependency_type="import",
                ),

                Dependency(
                    source="controller.user_controller",
                    target="dto.user_dto",
                    dependency_type="import",
                ),

                Dependency(
                    source="repository.user_repository",
                    target="models.user",
                    dependency_type="import",
                ),

            ]

        )

        #
        # Circular dependency example
        #

        graph.dependencies.extend(

            [

                Dependency(
                    source="moduleA",
                    target="moduleB",
                    dependency_type="import",
                ),

                Dependency(
                    source="moduleB",
                    target="moduleC",
                    dependency_type="import",
                ),

                Dependency(
                    source="moduleC",
                    target="moduleA",
                    dependency_type="import",
                ),

            ]

        )

        graph.circular_dependencies = [

            [
                "moduleA",
                "moduleB",
                "moduleC",
                "moduleA",
            ]

        ]

        print("✓ Sample dependency graph created")

        print()

        return graph

    # ---------------------------------------------------------

    def execute_architecture_analysis(self):
        """
        Execute the Architecture Analyzer.
        """

        print("Running Architecture Analyzer...")
        print()

        graph = self.create_sample_graph()

        try:

            #
            # Execute analyzer
            #

            analysis_result = self.analyzer.execute(graph)
            print("Errors:", analysis_result.errors)
            print("Metadata:", analysis_result.metadata)
            print("✓ Architecture analysis completed")
            print()

            self.tests_passed += 1

            return analysis_result

        except Exception as ex:

            self.tests_failed += 1

            print("✗ Architecture analysis failed")
            print(ex)

            raise

    # ---------------------------------------------------------

    def generate_console_report(
        self,
        analysis_result,
    ):
        """
        Print Architecture Report.
        """

        print("Generating Console Report...")
        print()

        try:

            report = self.reporter.build_report(
                analysis_result
            )

            self.reporter.print(report)

            print()

            print("✓ Console report generated")
            print()

            self.tests_passed += 1

            return report

        except Exception as ex:

            self.tests_failed += 1

            print("✗ Console report failed")
            print(ex)

            raise

    # ---------------------------------------------------------

    def generate_markdown_report(
        self,
        report,
    ):
        """
        Generate markdown report.
        """

        print("Generating Markdown Report...")
        print()

        try:

            markdown = self.reporter.render_markdown(
                report
            )

            output_file = (
                self.report_directory
                / "pf01_architecture_report.md"
            )

            output_file.write_text(
                markdown,
                encoding="utf-8",
            )

            print(
                f"✓ Markdown report saved to {output_file}"
            )

            print()

            self.tests_passed += 1

        except Exception as ex:

            self.tests_failed += 1

            print("✗ Markdown generation failed")
            print(ex)

            raise

    # ---------------------------------------------------------

    def print_summary(self):
        """
        Print regression summary.
        """

        print()
        print("=" * 70)
        print("Platform Foundation Regression Summary")
        print("=" * 70)
        print()

        total = self.tests_passed + self.tests_failed

        print(f"Total Tests : {total}")
        print(f"Passed      : {self.tests_passed}")
        print(f"Failed      : {self.tests_failed}")

        print()

        if self.tests_failed == 0:

            print("Overall Status : SUCCESS")

        else:

            print("Overall Status : FAILED")

        print()
        print("=" * 70)

    # ---------------------------------------------------------

    def run(self):
        """
        Execute the complete regression suite.
        """

        self.banner()

        analysis_result = (
            self.execute_architecture_analysis()
        )

        report = self.generate_console_report(
            analysis_result
        )

        self.generate_markdown_report(
            report
        )

        self.print_summary()

def main():
    """
    Entry point.
    """

    suite = PF01RegressionSuite()

    suite.run()


if __name__ == "__main__":

    main()
