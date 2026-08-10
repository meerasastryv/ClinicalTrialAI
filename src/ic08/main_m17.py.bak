from src.ic08.repositories.intelligence_repository import IntelligenceRepository
from src.ic08.services.customer_intelligence_service import (
    CustomerIntelligenceService,
)


from src.ic08.services.executive_summary_service import (
    ExecutiveSummaryService,
)
from src.ic08.repositories.customer_repository import CustomerRepository

from src.ic08.models.customer import Customer

def print_separator():
    print("=" * 70)


def print_section(title: str):
    print(f"\n{title}")
    print("-" * 70)


def main():
    print_separator()
    print("      CLINICALTRIALAI - INTELLIGENCE DASHBOARD")
    print("               IC-08 : Milestone 17")
    print_separator()

    # ---------------------------------------------------------
    # Create repository and services
    # ---------------------------------------------------------

    customer_repository = CustomerRepository()
    intelligence_repository = IntelligenceRepository()
    intelligence_service = CustomerIntelligenceService(customer_repository,intelligence_repository)

    summary_service = ExecutiveSummaryService()


    customer = Customer(customer_id="CUST-001",customer_name="ABC Pharma",organization="ABC Pharma",
        industry="Pharmaceutical",subscription_plan="Enterprise",region="North America",)

    customer_repository.add_customer(customer)


    # ---------------------------------------------------------
    # Build Dashboard
    # ---------------------------------------------------------
    dashboard = intelligence_service.build_dashboard("CUST-001")
    
    # ---------------------------------------------------------
    # Generate Executive Summary
    # ---------------------------------------------------------

    dashboard.executive_summary = summary_service.generate_summary(
        dashboard
    )

    # ---------------------------------------------------------
    # Display Dashboard
    # ---------------------------------------------------------

    print_section("ORGANIZATION")

    print(f"Customer ID       : {dashboard.customer_id}")
    print(f"Organization      : {dashboard.organization_name}")
    print(f"Study ID          : {dashboard.study_id}")
    print(f"Study Name        : {dashboard.study_name}")

    print_section("INTELLIGENCE SCORES")

    print(f"Health Score      : {dashboard.health_score:.1f}")
    print(f"Engagement Score  : {dashboard.engagement_score:.1f}")
    print(f"Adoption Score    : {dashboard.adoption_score:.1f}")
    print(f"Workflow Score    : {dashboard.workflow_score:.1f}")
    print(f"Journey Score     : {dashboard.journey_score:.1f}")
    print(f"Study Health      : {dashboard.study_health_score:.1f}")

    print_section("OVERALL")

    print(f"Overall Score     : {dashboard.overall_score:.2f}")
    print(f"Risk Level        : {dashboard.risk_level}")

    print_section("USAGE")

    print(f"Users             : {dashboard.total_users}")
    print(f"Sessions          : {dashboard.active_sessions}")
    print(
        f"Avg Duration      : "
        f"{dashboard.average_session_duration:.1f} minutes"
    )

    print_section("WORKFLOW")

    print(
        f"Completion        : "
        f"{dashboard.workflow_completion:.1f}%"
    )

    print_section("JOURNEY")

    print(
        f"Completion        : "
        f"{dashboard.journey_completion:.1f}%"
    )

    print(
        f"Drop-off Rate     : "
        f"{dashboard.drop_off_rate:.1f}%"
    )

    print_section("TOP FEATURES")

    for feature in dashboard.top_features:
        print(f"✓ {feature}")

    print_section("LEAST USED FEATURES")

    for feature in dashboard.least_used_features:
        print(f"• {feature}")

    print_section("RECOMMENDATIONS")

    for recommendation in dashboard.recommendations:
        print(f"• {recommendation}")

    print_section("EXECUTIVE SUMMARY")

    print(dashboard.executive_summary)

    print_separator()
    print("Milestone 17 Completed Successfully")
    print_separator()


if __name__ == "__main__":
    main()
