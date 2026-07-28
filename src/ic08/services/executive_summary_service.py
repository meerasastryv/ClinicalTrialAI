from typing import List

from src.ic08.models.customer_intelligence import CustomerIntelligence


class ExecutiveSummaryService:
    """
    Generates an executive summary from the consolidated
    CustomerIntelligence dashboard.

    NOTE:
    During the IC-08 refactoring milestone this service will be
    renamed to StudyExecutiveSummaryService.
    """

    def generate_summary(
        self,
        dashboard: CustomerIntelligence
    ) -> str:
        """
        Generate an executive summary for the dashboard.
        """

        lines: List[str] = []

        # ---------------------------------------------------------
        # Introduction
        # ---------------------------------------------------------

        lines.append(
            f"{dashboard.organization_name} demonstrates an "
            f"overall intelligence score of "
            f"{dashboard.overall_score:.1f}."
        )

        if dashboard.study_name:
            lines.append(
                f"Study '{dashboard.study_name}' "
                f"has been included in this assessment."
            )

        # ---------------------------------------------------------
        # Health
        # ---------------------------------------------------------

        if dashboard.health_score >= 90:
            lines.append(
                "Customer health is excellent."
            )
        elif dashboard.health_score >= 75:
            lines.append(
                "Customer health is stable."
            )
        else:
            lines.append(
                "Customer health requires attention."
            )

        # ---------------------------------------------------------
        # Engagement
        # ---------------------------------------------------------

        lines.append(
            f"There are {dashboard.total_users} active users "
            f"across {dashboard.active_sessions} sessions "
            f"with an average session duration of "
            f"{dashboard.average_session_duration:.1f} minutes."
        )

        # ---------------------------------------------------------
        # Workflow
        # ---------------------------------------------------------

        if dashboard.workflow_completion >= 90:
            lines.append(
                "Workflow execution is progressing efficiently."
            )
        elif dashboard.workflow_completion >= 75:
            lines.append(
                "Workflow execution is progressing steadily."
            )
        else:
            lines.append(
                "Workflow completion should be improved."
            )

        # ---------------------------------------------------------
        # Journey
        # ---------------------------------------------------------

        lines.append(
            f"Journey completion is "
            f"{dashboard.journey_completion:.1f}% "
            f"with a drop-off rate of "
            f"{dashboard.drop_off_rate:.1f}%."
        )

        # ---------------------------------------------------------
        # Features
        # ---------------------------------------------------------

        if dashboard.top_features:
            lines.append(
                "Most adopted features include "
                + ", ".join(dashboard.top_features)
                + "."
            )

        if dashboard.least_used_features:
            lines.append(
                "Features requiring additional adoption include "
                + ", ".join(dashboard.least_used_features)
                + "."
            )

        # ---------------------------------------------------------
        # Risk
        # ---------------------------------------------------------

        lines.append(
            f"The overall operational risk is "
            f"{dashboard.risk_level}."
        )

        # ---------------------------------------------------------
        # Recommendations
        # ---------------------------------------------------------

        if dashboard.recommendations:
            lines.append("Recommended actions:")

            for recommendation in dashboard.recommendations:
                lines.append(f"- {recommendation}")

        return "\n".join(lines)
