"""
architecture_reporter.py

Architecture Intelligence Reporter
"""

from ct_platform.framework.base_reporter import BaseReporter
from ct_platform.framework.analysis_result import AnalysisResult
from ct_platform.models.architecture_report import ArchitectureReport


class ArchitectureReporter(BaseReporter):

    def __init__(self, output_dir):
        """
        Initialize the reporter.
        """
        super().__init__(output_dir)
    """
    Reporter for Architecture Intelligence.
    """

    def build_report(
        self,
        analysis_result: AnalysisResult,
    ) -> ArchitectureReport:
        """
        Extract the strongly typed report.
        """

        return analysis_result.metadata[
            "architecture_report"
        ]

    def render_markdown(
        self,
        report: ArchitectureReport,
    ) -> str:
        """
        Generate Markdown report.
        """

        lines = []

        lines.append("# ClinicalTrialAI Architecture Report")
        lines.append("")

        lines.append(
            f"**Engine** : {report.engine_id}"
        )

        lines.append("")

        lines.append(
            f"**Health Score** : "
            f"{report.health_score:.1f}/100"
        )

        lines.append(
            f"**Rating** : {report.rating}"
        )

        lines.append("")

        #
        # ---------------------------------------------------------
        # Dependency Summary
        # ---------------------------------------------------------
        #

        lines.append("## Dependency Summary")
        lines.append("")

        lines.append(
            f"- Total Dependencies : "
            f"{report.total_dependencies}"
        )

        lines.append(
            f"- Internal : "
            f"{report.internal_dependencies}"
        )

        lines.append(
            f"- External : "
            f"{report.external_dependencies}"
        )

        lines.append(
            "- Standard Library : "
            f"{report.standard_library_dependencies}"
        )

        lines.append("")

        #
        # ---------------------------------------------------------
        # Circular Dependencies
        # ---------------------------------------------------------
        #

        lines.append(
            "## Circular Dependencies"
        )

        lines.append("")

        if report.circular_dependencies:

            for cycle in report.circular_dependencies:

                if isinstance(cycle, (list, tuple)):

                    lines.append(
                        "- "
                        + " -> ".join(cycle)
                    )

                else:

                    lines.append(
                        f"- {cycle}"
                    )

        else:

            lines.append("- None")

        lines.append("")

        #
        # ---------------------------------------------------------
        # Fan-Out
        # ---------------------------------------------------------
        #

        lines.append("## Top Fan-Out")
        lines.append("")

        for module, count in report.fan_out.items():

            lines.append(
                f"- {module}: {count}"
            )

        lines.append("")

        #
        # ---------------------------------------------------------
        # Fan-In
        # ---------------------------------------------------------
        #

        lines.append("## Top Fan-In")
        lines.append("")

        for module, count in report.fan_in.items():

            lines.append(
                f"- {module}: {count}"
            )

        lines.append("")

        #
        # ---------------------------------------------------------
        # Dependency Intelligence
        # ---------------------------------------------------------
        #

        intelligence = getattr(
            report,
            "dependency_intelligence",
            None,
        )

        if intelligence:

            lines.append(
                "## Dependency Intelligence"
            )

            lines.append("")

            #
            # Hotspots
            #

            if intelligence.hotspots:

                lines.append(
                    "### Architectural Hotspots"
                )

                lines.append("")

                for hotspot in (
                    intelligence.hotspots
                ):

                    lines.append(
                        f"- {hotspot.module}"
                    )

                    lines.append(
                        f"  - Score : "
                        f"{hotspot.score}"
                    )

                    lines.append(
                        f"  - {hotspot.reason}"
                    )

                lines.append("")

            #
            # Module Metrics
            #

            if intelligence.module_metrics:

                lines.append(
                    "### Module Metrics"
                )

                lines.append("")

                modules = sorted(
                    intelligence.module_metrics.values(),
                    key=lambda m: (
                        m.fan_in + m.fan_out
                    ),
                    reverse=True,
                )

                for module in modules:

                    lines.append(
                        f"#### {module.name}"
                    )

                    lines.append(
                        f"- Fan In : "
                        f"{module.fan_in}"
                    )

                    lines.append(
                        f"- Fan Out : "
                        f"{module.fan_out}"
                    )

                    lines.append(
                        f"- Instability : "
                        f"{module.instability}"
                    )

                    lines.append(
                        f"- Risk : "
                        f"{module.risk}"
                    )

                    lines.append(
                        f"- In Cycle : "
                        f"{module.in_cycle}"
                    )

                    lines.append("")

            #
            # Cycles
            #

            if intelligence.circular_dependencies:

                lines.append(
                    "### Intelligence Cycles"
                )

                lines.append("")

                for cycle in (
                    intelligence.circular_dependencies
                ):

                    lines.append(
                        "- "
                        + " -> ".join(
                            cycle.modules
                        )
                    )

                lines.append("")

            #
            # Layer Violations
            #

            if intelligence.layer_violations:

                lines.append(
                    "### Layer Violations"
                )

                lines.append("")

                for violation in (
                    intelligence.layer_violations
                ):

                    lines.append(
                        f"- {violation.source}"
                    )

                    lines.append(
                        f"  -> {violation.target}"
                    )

                    lines.append(
                        f"  ({violation.reason})"
                    )

                lines.append("")

            #
            # Intelligence Recommendations
            #

            if intelligence.recommendations:

                lines.append(
                    "### Intelligence Recommendations"
                )

                lines.append("")

                for recommendation in (
                    intelligence.recommendations
                ):

                    lines.append(
                        f"- {recommendation}"
                    )

                lines.append("")

        #
        # ---------------------------------------------------------
        # Warnings
        # ---------------------------------------------------------
        #

        if report.warnings:

            lines.append("## Warnings")
            lines.append("")

            for warning in report.warnings:

                lines.append(
                    f"- {warning}"
                )

            lines.append("")

        #
        # ---------------------------------------------------------
        # Recommendations
        # ---------------------------------------------------------
        #

        if report.recommendations:

            lines.append(
                "## Recommendations"
            )

            lines.append("")

            for recommendation in (
                report.recommendations
            ):

                lines.append(
                    f"- {recommendation}"
                )

            lines.append("")

        return "\n".join(lines)

    def print(
        self,
        report: ArchitectureReport,
    ):
        """
        Console output.
        """

        print()
        print("=" * 60)
        print(
            "ClinicalTrialAI Architecture Report"
        )
        print("=" * 60)
        print()

        print(
            f"Engine                     : "
            f"{report.engine_id}"
        )

        print(
            f"Dependencies               : "
            f"{report.total_dependencies}"
        )

        print(
            f"Internal Dependencies      : "
            f"{report.internal_dependencies}"
        )

        print(
            f"External Dependencies      : "
            f"{report.external_dependencies}"
        )

        print(
            "Standard Library           : "
            f"{report.standard_library_dependencies}"
        )

        print()

        print("Circular Dependencies")

        if report.circular_dependencies:

            for cycle in (
                report.circular_dependencies
            ):

                if isinstance(
                    cycle,
                    (list, tuple),
                ):

                    print(
                        " -> ".join(cycle)
                    )

                else:

                    print(cycle)

        else:

            print("None")

        print()
        print("Top Fan-Out")

        for module, count in (
            report.fan_out.items()
        ):

            print(
                f"  {module:45} {count}"
            )

        print()
        print("Top Fan-In")

        for module, count in (
            report.fan_in.items()
        ):

            print(
                f"  {module:45} {count}"
            )

        intelligence = getattr(
            report,
            "dependency_intelligence",
            None,
        )

        if intelligence:

            print()
            print("=" * 60)
            print(
                "Dependency Intelligence"
            )
            print("=" * 60)

            if intelligence.hotspots:

                print()
                print(
                    "Architectural Hotspots"
                )

                for hotspot in (
                    intelligence.hotspots
                ):

                    print(
                        f"  {hotspot.module}"
                    )

                    print(
                        f"     Score : "
                        f"{hotspot.score}"
                    )

                    print(
                        f"     {hotspot.reason}"
                    )

            if intelligence.circular_dependencies:

                print()
                print(
                    "Circular Dependencies"
                )

                for cycle in (
                    intelligence.circular_dependencies
                ):

                    print(
                        "  "
                        + " -> ".join(
                            cycle.modules
                        )
                    )

            if intelligence.layer_violations:

                print()
                print(
                    "Layer Violations"
                )

                for violation in (
                    intelligence.layer_violations
                ):

                    print(
                        f"  {violation.source}"
                    )

                    print(
                        f"    -> "
                        f"{violation.target}"
                    )

                    print(
                        f"    {violation.reason}"
                    )

            if intelligence.recommendations:

                print()
                print(
                    "Intelligence Recommendations"
                )

                for recommendation in (
                    intelligence.recommendations
                ):

                    print(
                        f"  • {recommendation}"
                    )

        print()
        print("=" * 60)
        print("Architecture Health")
        print("=" * 60)

        print()

        print(
            f"Health Score : "
            f"{report.health_score:.1f}/100"
        )

        print(
            f"Rating       : "
            f"{report.rating}"
        )

        if report.warnings:

            print()
            print("Warnings")

            for warning in report.warnings:

                print(
                    f"  • {warning}"
                )

        if report.recommendations:

            print()
            print("Recommendations")

            for recommendation in (
                report.recommendations
            ):

                print(
                    f"  • {recommendation}"
                )
