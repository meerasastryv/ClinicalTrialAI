from src.ic08.models.customer import Customer
from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.intelligence_repository import IntelligenceRepository
from src.ic08.repositories.report_repository import ReportRepository
from src.ic08.services.customer_intelligence_service import CustomerIntelligenceService
from src.ic08.services.executive_summary_service import ExecutiveSummaryService
from src.ic08.services.intelligence_report_service import IntelligenceReportService


def main():

    # ------------------------------------------------------------------
    # Create repositories
    # ------------------------------------------------------------------

    customer_repository = CustomerRepository()
    intelligence_repository = IntelligenceRepository()
    report_repository = ReportRepository()

    # ------------------------------------------------------------------
    # Add sample customer
    # ------------------------------------------------------------------

    customer = Customer(
        customer_id="CUST-001",
        customer_name="ABC Pharma",
        organization="ABC Pharma",
        industry="Pharmaceutical",
        subscription_plan="Enterprise",
        region="North America",
    )

    customer_repository.add_customer(customer)

    # ------------------------------------------------------------------
    # Create services
    # ------------------------------------------------------------------

    dashboard_service = CustomerIntelligenceService(
        customer_repository,
        intelligence_repository,
    )

    summary_service = ExecutiveSummaryService()

    report_service = IntelligenceReportService(
        report_repository
    )

    # ------------------------------------------------------------------
    # Build dashboard
    # ------------------------------------------------------------------

    dashboard = dashboard_service.build_dashboard("CUST-001")

    dashboard.executive_summary = (
        summary_service.generate_summary(dashboard)
    )

    # ------------------------------------------------------------------
    # Generate report
    # ------------------------------------------------------------------

    report = report_service.generate_report(
        dashboard,
        report_format="TEXT"
    )

    # ------------------------------------------------------------------
    # Display report
    # ------------------------------------------------------------------

    print("\n" + "=" * 70)
    print("          INTELLIGENCE REPORT")
    print("=" * 70)

    print(f"Report ID           : {report.report_id}")
    print(f"Customer            : {report.organization_name}")
    print(f"Overall Score       : {report.overall_score:.2f}")
    print(f"Risk Level          : {report.risk_level}")
    print(f"Generated At        : {report.generated_at}")
    print()

    print("-" * 70)
    print("METRICS")
    print("-" * 70)

    for metric, value in report.metrics.items():
        print(f"{metric:<25}: {value}")

    print()

    print("-" * 70)
    print("RECOMMENDATIONS")
    print("-" * 70)

    for recommendation in report.recommendations:
        print(f"• {recommendation}")

    print()

    print("-" * 70)
    print("EXECUTIVE SUMMARY")
    print("-" * 70)
    print(report.executive_summary)

    print()

    print("-" * 70)
    print(f"Reports Stored : {report_service.report_count()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
