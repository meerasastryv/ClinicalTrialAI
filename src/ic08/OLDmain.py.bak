from src.ic08.repositories.feature_repository import (
    FeatureRepository,
)

from src.ic08.repositories.feature_adoption_repository import (
    FeatureAdoptionRepository,
)

from src.ic08.services.feature_tracking_service import (
    FeatureTrackingService,
)

from src.ic08.services.feature_adoption_service import (
    FeatureAdoptionService,
)

from src.ic08.reports.feature_adoption_report import (
    FeatureAdoptionReport,
)


def load_sample_data(
    tracking_service: FeatureTrackingService,
) -> None:
    """
    Populate sample feature usage.
    """

    # Dashboard
    for _ in range(25):
        tracking_service.record_feature_usage(
            "Dashboard",
            duration_ms=1200,
            success=True,
        )

    # Reports
    for _ in range(18):
        tracking_service.record_feature_usage(
            "Reports",
            duration_ms=900,
            success=True,
        )

    # Analytics
    for _ in range(15):
        tracking_service.record_feature_usage(
            "Analytics",
            duration_ms=1500,
            success=True,
        )

    # Export
    for _ in range(8):
        tracking_service.record_feature_usage(
            "Export",
            duration_ms=700,
            success=False,
        )

    # Notifications
    for _ in range(30):
        tracking_service.record_feature_usage(
            "Notifications",
            duration_ms=500,
            success=True,
        )


def main():

    print("\n" + "=" * 80)
    print("IC-08 CUSTOMER USAGE INTELLIGENCE ENGINE")
    print("Milestone 6 - Feature Adoption Analytics")
    print("=" * 80)

    #
    # Repositories
    #
    feature_repository = FeatureRepository()
    feature_adoption_repository = FeatureAdoptionRepository()

    #
    # Services
    #
    tracking_service = FeatureTrackingService(
        feature_repository,
    )

    feature_adoption_service = FeatureAdoptionService(
        tracking_service,
        feature_repository,
        feature_adoption_repository,
    )

    #
    # Load Sample Usage
    #
    load_sample_data(tracking_service)

    #
    # Build Analytics
    #
    feature_adoption_service.calculate_feature_adoption()

    #
    # Report
    #
    report = FeatureAdoptionReport(
        feature_adoption_service,
    )

    report.print_report()

    #
    # Dashboard
    #
    dashboard = feature_adoption_service.generate_dashboard()

    print("\n" + "=" * 80)
    print("DASHBOARD SUMMARY")
    print("=" * 80)

    print(f"Total Features       : {dashboard['statistics']['total_features']}")
    print(f"Average Adoption     : {dashboard['statistics']['average_adoption']:.2f}%")
    print(f"Overall Score        : {dashboard['statistics']['overall_score']:.2f}")

    print("\nTop Features")

    for feature in dashboard["top_features"]:
        print(
            f"{feature.feature_name:20}"
            f"Score={feature.score:.2f}"
        )

    print("\nLow Adoption Features")

    for feature in dashboard["low_adoption_features"]:
        print(
            f"{feature.feature_name:20}"
            f"Adoption={feature.adoption_rate:.2f}%"
        )

    print("\n" + "=" * 80)
    print("Milestone 6 Completed Successfully")
    print("=" * 80)


if __name__ == "__main__":
    main()
