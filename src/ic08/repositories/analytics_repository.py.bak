"""
analytics_repository.py

Aggregates analytics across all IC-08 repositories.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.ic08.models.feature_usage import FeatureUsage
from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.feedback_repository import FeedbackRepository
from src.ic08.repositories.feature_repository import FeatureRepository
from src.ic08.repositories.session_repository import SessionRepository
from src.ic08.repositories.usage_repository import UsageRepository
from src.ic08.repositories.workflow_repository import WorkflowRepository


class AnalyticsRepository:
    """
    Provides platform-wide analytics by aggregating data from repositories.
    """

    def __init__(
        self,
        customer_repository: CustomerRepository,
        session_repository: SessionRepository,
        usage_repository: UsageRepository,
        feature_repository: FeatureRepository,
        workflow_repository: WorkflowRepository,
        feedback_repository: FeedbackRepository,
    ) -> None:
        self._customer_repository = customer_repository
        self._session_repository = session_repository
        self._usage_repository = usage_repository
        self._feature_repository = feature_repository
        self._workflow_repository = workflow_repository
        self._feedback_repository = feedback_repository

    def total_customers(self) -> int:
        """
        Returns the total number of customers.
        """
        return self._customer_repository.total_customers()

    def active_customers(self) -> int:
        """
        Returns the number of active customers.
        """
        return len(self._customer_repository.get_active_customers())

    def total_sessions(self) -> int:
        """
        Returns the total number of sessions.
        """
        return self._session_repository.total_sessions()

    def active_sessions(self) -> int:
        """
        Returns the number of active sessions.
        """
        return len(self._session_repository.get_active_sessions())

    def total_events(self) -> int:
        """
        Returns the total number of usage events.
        """
        return self._usage_repository.total_events()

    def total_features(self) -> int:
        """
        Returns the total number of tracked features.
        """
        return self._feature_repository.total_features()

    def total_workflows(self) -> int:
        """
        Returns the total number of workflows.
        """
        return self._workflow_repository.total_workflows()

    def total_feedback(self) -> int:
        """
        Returns the total number of feedback records.
        """
        return self._feedback_repository.total_feedback()

    def average_customer_rating(self) -> float:
        """
        Returns the average customer feedback rating.
        """
        return self._feedback_repository.average_rating()

    def average_session_duration(self) -> float:
        """
        Returns the average session duration in seconds.
        """
        return self._session_repository.average_session_duration_seconds()

    def most_used_feature(self) -> Optional[FeatureUsage]:
        """
        Returns the most-used feature.
        """
        return self._feature_repository.get_most_used_feature()

    def dashboard_metrics(self) -> Dict[str, object]:
        """
        Returns a dictionary containing key dashboard metrics.
        """
        top_feature = self.most_used_feature()

        return {
            "customers": self.total_customers(),
            "active_customers": self.active_customers(),
            "sessions": self.total_sessions(),
            "active_sessions": self.active_sessions(),
            "events": self.total_events(),
            "features": self.total_features(),
            "workflows": self.total_workflows(),
            "feedback": self.total_feedback(),
            "average_rating": self.average_customer_rating(),
            "average_session_duration": self.average_session_duration(),
            "top_feature": (
                top_feature.feature_name
                if top_feature is not None
                else None
            ),
        }
