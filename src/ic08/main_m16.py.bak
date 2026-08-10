"""
IC-08 - Platform Usage Intelligence
Milestone 16 - Study Health Index
"""

from src.ic08.services.study_health_service import StudyHealthService


def print_separator():
    print("=" * 60)


def print_sub_separator():
    print("-" * 60)


def main():
    print_separator()
    print("IC-08 - Platform Usage Intelligence")
    print("Milestone 16 - Study Health Index")
    print_separator()

    service = StudyHealthService()

    study = service.calculate_health(
        study_id="ONC-PH3-001",
        programmer_productivity=91,
        workflow_completion=94,
        metadata_reuse=89,
        deliverable_completion=93,
        platform_usage_risk=12,
        history_count=25,
    )

    print("\nStudy Health Report")
    print_sub_separator()

    print(f"Study ID              : {study.study_id}")
    print(f"Health Score          : {study.health_score:.2f}")
    print(f"Status                : {study.status}")
    print(f"Risk Level            : {study.risk_level}")
    print(f"Confidence            : {study.confidence:.2%}")

    print_sub_separator()
    print("Key Indicators")
    print_sub_separator()

    for indicator in study.indicators:
        print(f"✓ {indicator}")

    print_sub_separator()
    print("Repository Statistics")
    print_sub_separator()

    print(f"Studies Evaluated     : {service.repository.count()}")
    print(f"Average Health Index  : {service.average_health():.2f}")

    print("\nTop Healthy Studies")

    for index, item in enumerate(
        service.top_healthy_studies(),
        start=1,
    ):
        print(
            f"{index}. "
            f"{item.study_id} "
            f"({item.health_score:.2f})"
        )

    print_separator()
    print("Milestone 16 completed successfully.")
    print_separator()


if __name__ == "__main__":
    main()
