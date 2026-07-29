from src.ic08.models.customer import Customer
from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.intelligence_repository import IntelligenceRepository
from src.ic08.repositories.report_repository import ReportRepository
from src.ic08.repositories.action_plan_repository import ActionPlanRepository

from src.ic08.services.customer_intelligence_service import CustomerIntelligenceService
from src.ic08.services.executive_summary_service import ExecutiveSummaryService
from src.ic08.services.intelligence_report_service import IntelligenceReportService
from src.ic08.services.action_plan_service import ActionPlanService


def main():

    # -------------------------------------------------------------
    # Repositories
    # -------------------------------------------------------------

    customer_repository = CustomerRepository()
    intelligence_repository = IntelligenceRepository()
    report_repository = ReportRepository()
    action_plan_repository = ActionPlanRepository()

    # -------------------------------------------------------------
    # Sample Customer
    # -------------------------------------------------------------

    customer = Customer(
        customer_id="CUST-001",
        customer_name="ABC Pharma",
        organization="ABC Pharma",
        industry="Pharmaceutical",
        subscription_plan="Enterprise",
        region="North America",
    )

    customer_repository.add_customer(customer)

    # -------------------------------------------------------------
    # Services
    # -------------------------------------------------------------

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

    # -------------------------------------------------------------
    # Dashboard
    # -------------------------------------------------------------

    dashboard = dashboard_service.build_dashboard("CUST-001")

    dashboard.executive_summary = (
        summary_service.generate_summary(dashboard)
    )

    # -------------------------------------------------------------
    # Intelligence Report
    # -------------------------------------------------------------

    report = report_service.generate_report(dashboard)

    # -------------------------------------------------------------
    # Action Plan
    # -------------------------------------------------------------

    action_plan = action_service.generate_action_plan(report)

    # -------------------------------------------------------------
    # Display
    # -------------------------------------------------------------

    print("\n" + "=" * 72)
    print("                ACTION PLAN")
    print("=" * 72)

    print(f"Action Plan ID   : {action_plan.action_plan_id}")
    print(f"Customer         : {action_plan.organization_name}")
    print(f"Overall Score    : {action_plan.overall_score:.2f}")
    print(f"Risk Level       : {action_plan.risk_level}")
    print(f"Priority         : {action_plan.priority}")
    print(f"Status           : {action_plan.status}")

    print("\n" + "-" * 72)
    print("ACTION ITEMS")
    print("-" * 72)

    for index, action in enumerate(action_plan.actions, start=1):
        print(f"{index}. {action}")

    print("\n" + "-" * 72)
    print("EXPECTED OUTCOME")
    print("-" * 72)
    print(action_plan.expected_outcome)

    print("\n" + "-" * 72)
    print(f"Stored Action Plans : {action_service.action_plan_count()}")

    print("=" * 72)


if __name__ == "__main__":
    main()
