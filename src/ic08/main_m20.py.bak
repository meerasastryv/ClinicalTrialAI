from src.ic08.models.customer import Customer

from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.intelligence_repository import IntelligenceRepository
from src.ic08.repositories.report_repository import ReportRepository
from src.ic08.repositories.action_plan_repository import ActionPlanRepository
from src.ic08.repositories.operational_decision_repository import (
    OperationalDecisionRepository,
)

from src.ic08.services.customer_intelligence_service import (
    CustomerIntelligenceService,
)
from src.ic08.services.executive_summary_service import (
    ExecutiveSummaryService,
)
from src.ic08.services.intelligence_report_service import (
    IntelligenceReportService,
)
from src.ic08.services.action_plan_service import (
    ActionPlanService,
)
from src.ic08.services.operational_decision_service import (
    OperationalDecisionService,
)


def main():

    # ---------------------------------------------------------
    # Repositories
    # ---------------------------------------------------------

    customer_repository = CustomerRepository()
    intelligence_repository = IntelligenceRepository()
    report_repository = ReportRepository()
    action_plan_repository = ActionPlanRepository()
    operational_decision_repository = (
        OperationalDecisionRepository()
    )

    # ---------------------------------------------------------
    # Sample Customer
    # ---------------------------------------------------------

    customer = Customer(
        customer_id="CUST-001",
        customer_name="ABC Pharma",
        organization="ABC Pharma",
        industry="Pharmaceutical",
        subscription_plan="Enterprise",
        region="North America",
    )

    customer_repository.add_customer(customer)

    # ---------------------------------------------------------
    # Services
    # ---------------------------------------------------------

    dashboard_service = CustomerIntelligenceService(
        customer_repository,
        intelligence_repository,
    )

    summary_service = ExecutiveSummaryService()

    report_service = IntelligenceReportService(
        report_repository
    )

    action_service = ActionPlanService(
        action_plan_repository
    )

    decision_service = OperationalDecisionService(
        operational_decision_repository
    )

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    dashboard = dashboard_service.build_dashboard(
        "CUST-001"
    )

    dashboard.executive_summary = (
        summary_service.generate_summary(dashboard)
    )

    # ---------------------------------------------------------
    # Report
    # ---------------------------------------------------------

    report = report_service.generate_report(dashboard)

    # ---------------------------------------------------------
    # Action Plan
    # ---------------------------------------------------------

    action_plan = action_service.generate_action_plan(
        report
    )

    # ---------------------------------------------------------
    # Operational Decision
    # ---------------------------------------------------------

    decision = (
        decision_service.generate_operational_decision(
            report,
            action_plan,
        )
    )

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    print("\n" + "=" * 80)
    print("          OPERATIONAL DECISION SUPPORT")
    print("=" * 80)

    print(f"Decision ID        : {decision.decision_id}")
    print(f"Customer           : {decision.organization_name}")
    print(f"Overall Score      : {decision.overall_score:.2f}")
    print(f"Risk Level         : {decision.risk_level}")
    print(f"Decision Status    : {decision.decision_status}")

    print("\n" + "-" * 80)
    print("EXECUTIVE SUMMARY")
    print("-" * 80)

    print(decision.executive_summary)

    print("\n" + "-" * 80)
    print("RECOMMENDED ACTIONS")
    print("-" * 80)

    for index, action in enumerate(
        decision.recommended_actions,
        start=1,
    ):
        print(f"{index}. {action}")

    print("\n" + "-" * 80)
    print("EXPECTED OUTCOME")
    print("-" * 80)

    print(decision.expected_outcome)

    print("\n" + "-" * 80)
    print(
        f"Operational Decisions Stored : "
        f"{decision_service.decision_count()}"
    )

    print("=" * 80)


if __name__ == "__main__":
    main()
