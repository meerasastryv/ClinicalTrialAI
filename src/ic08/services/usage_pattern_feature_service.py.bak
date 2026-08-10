"""
usage_pattern_feature_service.py

Builds the machine learning feature matrix for
customer usage pattern discovery.
"""

from typing import List

from src.ic08.models.feature_definition import FeatureDefinition
from src.ic08.models.feature_matrix import FeatureMatrix


class UsagePatternFeatureService:
    """
    Builds machine learning feature vectors from
    customer usage analytics.
    """
    def __init__(self,analytics_data: dict | None = None,):
        #def __init__(self):
        """Initialize feature engineering service."""
        # Store analytics data
        self._analytics_data = analytics_data or {}
        self._feature_definitions = (
            self._build_feature_catalog()
        )

        self._feature_pipeline = [
            self._calculate_session_count,
            self._calculate_average_session_duration,
            self._calculate_features_used,
            self._calculate_workflow_count,
            self._calculate_error_count,
            self._calculate_adoption_score,
        ]

    # ------------------------------------------------------------------
    # Feature Catalog
    # ------------------------------------------------------------------

    def _build_feature_catalog(
        self,
    ) -> List[FeatureDefinition]:
        """
        Define all machine learning features.
        """

        return [

            FeatureDefinition(
                name="session_count",
                description="Total number of sessions",
                source="CustomerSession",
            ),

            FeatureDefinition(
                name="average_session_duration",
                description="Average session duration",
                source="CustomerSession",
            ),

            FeatureDefinition(
                name="features_used",
                description="Number of unique features used",
                source="FeatureUsage",
            ),

            FeatureDefinition(
                name="workflow_count",
                description="Completed workflows",
                source="Workflow",
            ),

            FeatureDefinition(
                name="error_count",
                description="Total application errors",
                source="UsageEvent",
            ),

            FeatureDefinition(
                name="adoption_score",
                description="Feature adoption score",
                source="AdoptionMetric",
            ),
        ]

    # ------------------------------------------------------------------
    # Feature Matrix
    # ------------------------------------------------------------------
    def _get_metric(self,customer,metric_name: str,default=0.0,):
        """
        Retrieve a metric for a customer from the
        analytics data source.
        """
        customer_metrics = self._analytics_data.get(customer.customer_id,{},)
        return self._safe_float(customer_metrics.get(metric_name,default,))
    def build_feature_matrix(
        self,
        customers: List[object],
    ) -> FeatureMatrix:
        """
        Build the machine learning feature matrix.
        """

        feature_matrix = FeatureMatrix()

        feature_matrix.feature_definitions = (
            self.get_feature_definitions()
        )

        for customer in customers:

            row = []

            for calculator in self._feature_pipeline:
                row.append(
                    calculator(customer)
                )

            feature_matrix.customer_ids.append(
                str(customer.customer_id)
            )

            feature_matrix.feature_values.append(
                row
            )

        return feature_matrix

    # ------------------------------------------------------------------
    # Feature Access
    # ------------------------------------------------------------------

    def get_feature_definitions(
        self,
    ) -> List[FeatureDefinition]:
        """
        Return feature catalog.
        """

        return self._feature_definitions

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def _safe_float(
        self,
        value,
    ) -> float:
        """
        Safely convert a value to float.
        """

        if value is None:
            return 0.0

        try:
            return float(value)

        except (TypeError, ValueError):
            return 0.0

    # ------------------------------------------------------------------
    # Feature Calculators
    # ------------------------------------------------------------------

    def _calculate_session_count(
        self,
        customer,
    ) -> float:
        """
        Calculate total sessions.
        """
        return self._get_metric(customer,"session_count",)

    def _calculate_average_session_duration(
        self,
        customer,
    ) -> float:
        """
        Calculate average session duration.
        """
        return self._get_metric(customer,"average_session_duration",)

    def _calculate_features_used(
        self,
        customer,
    ) -> float:
        """
        Calculate number of unique features used.
        """
        return self._get_metric(customer,"features_used",)

    def _calculate_workflow_count(
        self,
        customer,
    ) -> float:
        """
        Calculate completed workflows.
        """
        return self._get_metric(customer,"workflow_count",)
    def _calculate_error_count(
        self,
        customer,
    ) -> float:
        """
        Calculate application errors.
        """
        return self._get_metric(customer,"error_count",)

    def _calculate_adoption_score(
        self,
        customer,
    ) -> float:
        """
        Calculate feature adoption score.
        """

        return self._get_metric(customer,"adoption_score",)
