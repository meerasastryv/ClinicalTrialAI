"""
main_m11.py

IC-08 – Milestone 11
Intelligent Usage Pattern Discovery

Demonstrates machine learning based customer
usage pattern discovery using DBSCAN clustering.
"""

from src.ic08.models.customer import Customer
from src.ic08.repositories.usage_pattern_repository import (
    UsagePatternRepository,
)
from src.ic08.services.usage_pattern_feature_service import (
    UsagePatternFeatureService,
)
from src.ic08.services.usage_pattern_discovery_service import (
    UsagePatternDiscoveryService,
)


# ---------------------------------------------------------
# Sample Data
# ---------------------------------------------------------

def build_sample_customers():
    """
    Build sample customers.
    """

    return [

        Customer(
            customer_id="C001",
            customer_name="ABC Pharma",
            organization="ABC Pharma",
            industry="Healthcare",
            subscription_plan="Enterprise",
            region="USA",
        ),

        Customer(
            customer_id="C002",
            customer_name="XYZ Biotech",
            organization="XYZ Biotech",
            industry="Biotechnology",
            subscription_plan="Professional",
            region="UK",
        ),

        Customer(
            customer_id="C003",
            customer_name="Global Clinical",
            organization="Global Clinical",
            industry="Healthcare",
            subscription_plan="Enterprise",
            region="Germany",
        ),

        Customer(
            customer_id="C004",
            customer_name="Life Sciences Inc",
            organization="Life Sciences",
            industry="Pharmaceutical",
            subscription_plan="Standard",
            region="India",
        ),

        Customer(
            customer_id="C005",
            customer_name="Health Analytics",
            organization="Health Analytics",
            industry="Healthcare",
            subscription_plan="Enterprise",
            region="Canada",
        ),

    ]


def build_sample_analytics():
    """
    Sample analytics used for feature engineering.
    """

    return {

        "C001": {
            "session_count": 25,
            "average_session_duration": 42,
            "features_used": 10,
            "workflow_count": 12,
            "error_count": 1,
            "adoption_score": 0.92,
        },

        "C002": {
            "session_count": 22,
            "average_session_duration": 40,
            "features_used": 9,
            "workflow_count": 11,
            "error_count": 1,
            "adoption_score": 0.88,
        },

        "C003": {
            "session_count": 5,
            "average_session_duration": 12,
            "features_used": 3,
            "workflow_count": 2,
            "error_count": 7,
            "adoption_score": 0.31,
        },

        "C004": {
            "session_count": 6,
            "average_session_duration": 14,
            "features_used": 2,
            "workflow_count": 3,
            "error_count": 5,
            "adoption_score": 0.35,
        },

        "C005": {
            "session_count": 24,
            "average_session_duration": 43,
            "features_used": 11,
            "workflow_count": 13,
            "error_count": 0,
            "adoption_score": 0.95,
        },

    }


# ---------------------------------------------------------
# Reporting Helpers
# ---------------------------------------------------------

def print_header():
    """
    Print report header.
    """

    print()
    print("=" * 70)
    print("IC-08 - Milestone 11")
    print("Intelligent Usage Pattern Discovery")
    print("=" * 70)


def print_summary(result):
    """
    Print discovery summary.
    """

    print()
    print("Discovery Summary")
    print("-" * 70)

    print(f"Algorithm          : {result.algorithm}")
    print(f"Customers          : {result.customer_count}")
    print(f"Features           : {result.feature_count}")
    print(f"Clusters           : {result.cluster_count}")
    print(f"Noise Customers    : {result.noise_count}")
    print(f"Execution Time     : {result.execution_time:.4f} sec")


def print_clusters(result):
    """
    Print cluster assignments.
    """

    print()
    print("Cluster Assignments")
    print("-" * 70)

    for cluster in result.clusters:

        label = (
            "Noise"
            if cluster.is_noise
            else f"Cluster {cluster.cluster_id}"
        )

        print(
            f"{cluster.customer_id:<8} -> {label}"
        )


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

def main():
    """
    Execute Milestone 11 demonstration.
    """

    print_header()

    customers = build_sample_customers()

    analytics_data = build_sample_analytics()

    repository = UsagePatternRepository()

    feature_service = UsagePatternFeatureService(
        analytics_data=analytics_data
    )
    discovery_service = UsagePatternDiscoveryService(repository=repository,eps=2.0,min_samples=2,)
    print()
    print("DBSCAN Configuration")
    print("--------------------")
    print("eps         :", discovery_service._eps)
    print("min_samples :", discovery_service._min_samples)
    print()
    print("Building feature matrix...")

    feature_matrix = feature_service.build_feature_matrix(
        customers
    )

    print(
        f"Customers processed : "
        f"{len(feature_matrix.customer_ids)}"
    )

    print(
        f"Features generated  : "
        f"{len(feature_matrix.feature_definitions)}"
    )

    print()
    print("Running DBSCAN clustering...")
    print()
    print("Feature Matrix")
    print("-" * 70)
    for customer_id, values in zip(
        feature_matrix.customer_ids,feature_matrix.feature_values,):
        print(customer_id, values)
    result = discovery_service.discover_patterns(feature_matrix)
    print_summary(result)
    print_clusters(result)
    print()
    print("=" * 70)
    print("Milestone 11 completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()

    except Exception as ex:

        print()
        print("=" * 70)
        print("Milestone 11 FAILED")
        print("=" * 70)
        print(ex)


