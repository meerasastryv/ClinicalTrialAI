"""
feature_usage_analytics_service.py

Feature Usage Analytics Service

Provides analytics over customer usage events including:

- Feature usage statistics
- Customer analytics
- Workflow analytics
- Usage trends
- Feature adoption
- Success and failure metrics
- Power user identification
"""

from __future__ import annotations

import logging

from collections import Counter
from collections import defaultdict
from datetime import datetime
from statistics import mean
from typing import Any

from src.ic08.models.usage_event import UsageEvent
from src.ic08.services.feature_tracking_service import (
    FeatureTrackingService,
)
from src.ic08.services.session_tracking_service import (
    SessionTrackingService,
)
from src.ic08.services.usage_event_service import (
    UsageEventService,
)
from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)

logger = logging.getLogger(__name__)


class FeatureUsageAnalyticsService:
    """
    Provides feature usage analytics for Customer Usage Intelligence.

    This service computes statistics including:

    - Feature usage
    - Customer distribution
    - Workflow distribution
    - Adoption
    - Trends
    - Power users
    """

    def __init__(
        self,
        usage_event_service: UsageEventService,
        feature_tracking_service: FeatureTrackingService | None = None,
        workflow_tracking_service: WorkflowTrackingService | None = None,
        session_tracking_service: SessionTrackingService | None = None,
    ) -> None:
        """
        Initialize analytics service.
        """

        self._usage_service = usage_event_service
        self._feature_service = feature_tracking_service
        self._workflow_service = workflow_tracking_service
        self._session_service = session_tracking_service

        logger.info(
            "FeatureUsageAnalyticsService initialized."
        )

    ####################################################################
    # Event Collection
    ####################################################################

    def _collect_events(
        self,
    ) -> list[UsageEvent]:
        """
        Returns all recorded usage events.
        """

        events = self._usage_service.get_all_events()

        logger.debug(
            "Collected %d usage events.",
            len(events),
        )

        return events

    ####################################################################
    # Grouping Helpers
    ####################################################################

    def _group_by_feature(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by feature.
        """

        grouped = defaultdict(list)

        for event in events:
            grouped[event.feature_name].append(event)

        return dict(grouped)

    def _group_by_customer(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by customer.
        """

        grouped = defaultdict(list)

        for event in events:
            grouped[event.customer_id].append(event)

        return dict(grouped)

    def _group_by_session(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by session.
        """

        grouped = defaultdict(list)

        for event in events:
            grouped[event.session_id].append(event)

        return dict(grouped)

    def _group_by_workflow(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by workflow.

        Workflow name is expected in metadata.
        """

        grouped = defaultdict(list)

        for event in events:
            workflow = event.metadata.get(
                "workflow_name",
                "Unknown",
            )

            grouped[workflow].append(event)

        return dict(grouped)

    ####################################################################
    # Time Grouping
    ####################################################################

    def _group_by_hour(
        self,
        events: list[UsageEvent],
    ) -> dict[int, int]:
        """
        Groups events by hour.
        """

        counter = Counter()

        for event in events:
            counter[event.timestamp.hour] += 1

        return dict(sorted(counter.items()))

    def _group_by_day(
        self,
        events: list[UsageEvent],
    ) -> dict[str, int]:
        """
        Groups events by weekday.
        """

        counter = Counter()

        for event in events:
            counter[event.timestamp.strftime("%A")] += 1

        return dict(counter)

    def _group_by_week(
        self,
        events: list[UsageEvent],
    ) -> dict[str, int]:
        """
        Groups events by ISO week.
        """

        counter = Counter()

        for event in events:
            week = event.timestamp.isocalendar().week
            counter[f"Week {week}"] += 1

        return dict(counter)

    def _group_by_month(
        self,
        events: list[UsageEvent],
    ) -> dict[str, int]:
        """
        Groups events by month.
        """

        counter = Counter()

        for event in events:
            counter[event.timestamp.strftime("%b")] += 1

        return dict(counter)

    ####################################################################
    # Calculation Helpers
    ####################################################################

    def _calculate_success_rate(
        self,
        events: list[UsageEvent],
    ) -> float:
        """
        Calculates success rate.
        """

        if not events:
            return 0.0

        success = sum(
            1 for event in events if event.success
        )

        return round(
            success * 100 / len(events),
            2,
        )

    def _calculate_failure_rate(
        self,
        events: list[UsageEvent],
    ) -> float:
        """
        Calculates failure rate.
        """

        if not events:
            return 0.0

        failed = sum(
            1 for event in events if not event.success
        )

        return round(
            failed * 100 / len(events),
            2,
        )

    def _calculate_average_duration(
        self,
        events: list[UsageEvent],
    ) -> float:
        """
        Returns average execution duration.
        """

        if not events:
            return 0.0

        return round(
            mean(
                event.duration_ms
                for event in events
            ),
            2,
        )

    def _calculate_adoption(
        self,
        feature_events: list[UsageEvent],
        all_events: list[UsageEvent],
    ) -> float:
        """
        Calculates feature adoption percentage.
        """

        if not all_events:
            return 0.0

        total_users = {
            event.customer_id
            for event in all_events
        }

        feature_users = {
            event.customer_id
            for event in feature_events
        }

        if not total_users:
            return 0.0

        return round(
            len(feature_users)
            * 100
            / len(total_users),
            2,
        )

    ####################################################################
    # Summary Builder
    ####################################################################

    def _build_summary(
        self,
        feature_name: str,
        feature_events: list[UsageEvent],
        all_events: list[UsageEvent],
    ) -> dict[str, Any]:
        """
        Builds a summary for one feature.
        """

        unique_customers = {
            event.customer_id
            for event in feature_events
        }

        unique_sessions = {
            event.session_id
            for event in feature_events
        }

        hourly = Counter(
            event.timestamp.hour
            for event in feature_events
        )

        weekday = Counter(
            event.timestamp.strftime("%A")
            for event in feature_events
        )

        return {
            "feature": feature_name,
            "total_usage": len(feature_events),
            "unique_customers": len(
                unique_customers
            ),
            "unique_sessions": len(
                unique_sessions
            ),
            "average_duration_ms":
                self._calculate_average_duration(
                    feature_events
                ),
            "success_rate":
                self._calculate_success_rate(
                    feature_events
                ),
            "failure_rate":
                self._calculate_failure_rate(
                    feature_events
                ),
            "adoption":
                self._calculate_adoption(
                    feature_events,
                    all_events,
                ),
            "peak_hour":
                hourly.most_common(1)[0][0]
                if hourly
                else None,
            "peak_day":
                weekday.most_common(1)[0][0]
                if weekday
                else None,
        }


    ####################################################################
    # Feature Statistics
    ####################################################################

    def calculate_feature_statistics(
        self,
    ) -> dict[str, dict[str, Any]]:
        """
        Calculates analytics for every feature.
        """

        logger.info(
            "Calculating feature statistics."
        )

        events = self._collect_events()

        grouped = self._group_by_feature(events)

        statistics = {}

        for feature_name, feature_events in grouped.items():

            statistics[feature_name] = (
                self._build_summary(
                    feature_name,
                    feature_events,
                    events,
                )
            )

        logger.info(
            "Calculated statistics for %d features.",
            len(statistics),
        )

        return statistics

    ####################################################################
    # Usage Summary
    ####################################################################

    def feature_usage_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns an overall feature usage summary.
        """

        logger.info(
            "Generating feature usage summary."
        )

        events = self._collect_events()

        statistics = self.calculate_feature_statistics()

        return {
            "total_events": len(events),
            "total_features": len(statistics),
            "total_customers": len(
                {
                    event.customer_id
                    for event in events
                }
            ),
            "total_sessions": len(
                {
                    event.session_id
                    for event in events
                }
            ),
            "successful_events": sum(
                1
                for event in events
                if event.success
            ),
            "failed_events": sum(
                1
                for event in events
                if not event.success
            ),
        }

    ####################################################################
    # Top Features
    ####################################################################

    def top_features(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Returns the most frequently used features.
        """

        statistics = self.calculate_feature_statistics()

        ordered = sorted(
            statistics.values(),
            key=lambda item: item["total_usage"],
            reverse=True,
        )

        return ordered[:limit]

    ####################################################################
    # Least Used Features
    ####################################################################

    def least_used_features(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Returns the least frequently used features.
        """

        statistics = self.calculate_feature_statistics()

        ordered = sorted(
            statistics.values(),
            key=lambda item: item["total_usage"],
        )

        return ordered[:limit]

    ####################################################################
    # Adoption
    ####################################################################

    def feature_adoption(
        self,
    ) -> dict[str, float]:
        """
        Returns adoption percentage for every feature.
        """

        logger.info(
            "Calculating feature adoption."
        )

        events = self._collect_events()

        grouped = self._group_by_feature(events)

        adoption = {}

        for feature_name, feature_events in grouped.items():

            adoption[feature_name] = (
                self._calculate_adoption(
                    feature_events,
                    events,
                )
            )

        return adoption

    ####################################################################
    # Feature Lookup
    ####################################################################

    def get_feature_statistics(
        self,
        feature_name: str,
    ) -> dict[str, Any]:
        """
        Returns statistics for a single feature.
        """

        statistics = self.calculate_feature_statistics()

        return statistics.get(
            feature_name,
            {},
        )

    ####################################################################
    # Feature Exists
    ####################################################################

    def feature_exists(
        self,
        feature_name: str,
    ) -> bool:
        """
        Checks whether usage has been recorded for a feature.
        """

        statistics = self.calculate_feature_statistics()

        return feature_name in statistics

    ####################################################################
    # Feature Event Count
    ####################################################################

    def feature_event_count(
        self,
        feature_name: str,
    ) -> int:
        """
        Returns number of recorded events for a feature.
        """

        events = self._collect_events()

        return sum(
            1
            for event in events
            if event.feature_name == feature_name
        )

    ####################################################################
    # Most Successful Features
    ####################################################################

    def most_successful_features(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Returns features ordered by success rate.
        """

        statistics = self.calculate_feature_statistics()

        ordered = sorted(
            statistics.values(),
            key=lambda item: item["success_rate"],
            reverse=True,
        )

        return ordered[:limit]

    ####################################################################
    # Most Failure-Prone Features
    ####################################################################

    def most_failure_prone_features(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Returns features ordered by failure rate.
        """

        statistics = self.calculate_feature_statistics()

        ordered = sorted(
            statistics.values(),
            key=lambda item: item["failure_rate"],
            reverse=True,
        )

        return ordered[:limit]

    ####################################################################
    # Customer Distribution
    ####################################################################

    def customer_distribution(
        self,
    ) -> dict[str, dict[str, int]]:
        """
        Returns feature usage distribution grouped by customer.
        """

        logger.info(
            "Generating customer distribution."
        )

        events = self._collect_events()

        grouped = self._group_by_customer(events)

        distribution: dict[str, dict[str, int]] = {}

        for customer_id, customer_events in grouped.items():

            feature_counter = Counter(
                event.feature_name
                for event in customer_events
            )

            distribution[customer_id] = dict(
                sorted(
                    feature_counter.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )

        return distribution

    ####################################################################
    # Workflow Distribution
    ####################################################################

    def workflow_distribution(
        self,
    ) -> dict[str, dict[str, int]]:
        """
        Returns feature usage grouped by workflow.
        """

        logger.info(
            "Generating workflow distribution."
        )

        events = self._collect_events()

        grouped = self._group_by_workflow(events)

        distribution: dict[str, dict[str, int]] = {}

        for workflow_name, workflow_events in grouped.items():

            feature_counter = Counter(
                event.feature_name
                for event in workflow_events
            )

            distribution[workflow_name] = dict(
                sorted(
                    feature_counter.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )

        return distribution

    ####################################################################
    # Hourly Usage
    ####################################################################

    def hourly_usage(
        self,
    ) -> dict[int, int]:
        """
        Returns usage counts by hour.
        """

        logger.info(
            "Generating hourly usage analytics."
        )

        return self._group_by_hour(
            self._collect_events()
        )

    ####################################################################
    # Daily Usage
    ####################################################################

    def daily_usage(
        self,
    ) -> dict[str, int]:
        """
        Returns usage counts by weekday.
        """

        logger.info(
            "Generating daily usage analytics."
        )

        return self._group_by_day(
            self._collect_events()
        )

    ####################################################################
    # Weekly Usage
    ####################################################################

    def weekly_usage(
        self,
    ) -> dict[str, int]:
        """
        Returns usage counts by ISO week.
        """

        logger.info(
            "Generating weekly usage analytics."
        )

        return self._group_by_week(
            self._collect_events()
        )

    ####################################################################
    # Monthly Usage
    ####################################################################

    def monthly_usage(
        self,
    ) -> dict[str, int]:
        """
        Returns usage counts by month.
        """

        logger.info(
            "Generating monthly usage analytics."
        )

        return self._group_by_month(
            self._collect_events()
        )

    ####################################################################
    # Power Users
    ####################################################################

    def power_users(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Returns customers with the highest usage activity.
        """

        logger.info(
            "Identifying power users."
        )

        events = self._collect_events()

        counter = Counter(
            event.customer_id
            for event in events
        )

        results = []

        for customer_id, usage_count in counter.most_common(limit):

            customer_events = [
                event
                for event in events
                if event.customer_id == customer_id
            ]

            successful_events = sum(
                1
                for event in customer_events
                if event.success
            )

            failed_events = len(customer_events) - successful_events

            unique_features = len(
                {
                    event.feature_name
                    for event in customer_events
                }
            )

            total_duration = sum(
                event.duration_ms
                for event in customer_events
            )

            results.append(
                {
                    "customer_id": customer_id,
                    "usage_count": usage_count,
                    "unique_features": unique_features,
                    "successful_events": successful_events,
                    "failed_events": failed_events,
                    "success_rate": round(
                        successful_events
                        * 100
                        / usage_count,
                        2,
                    ),
                    "average_duration_ms": round(
                        total_duration
                        / usage_count,
                        2,
                    ),
                }
            )

        return results

    ####################################################################
    # Peak Usage Information
    ####################################################################

    def peak_usage_hour(
        self,
    ) -> int | None:
        """
        Returns the hour with the highest usage.
        """

        hourly = self.hourly_usage()

        if not hourly:
            return None

        return max(
            hourly.items(),
            key=lambda item: item[1],
        )[0]

    def peak_usage_day(
        self,
    ) -> str | None:
        """
        Returns the weekday with the highest usage.
        """

        daily = self.daily_usage()

        if not daily:
            return None

        return max(
            daily.items(),
            key=lambda item: item[1],
        )[0]

    ####################################################################
    # Overall Trend Summary
    ####################################################################

    def trend_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a summary of usage trends.
        """

        return {
            "peak_hour": self.peak_usage_hour(),
            "peak_day": self.peak_usage_day(),
            "hourly_usage": self.hourly_usage(),
            "daily_usage": self.daily_usage(),
            "weekly_usage": self.weekly_usage(),
            "monthly_usage": self.monthly_usage(),
        }

    ####################################################################
    # Export - Feature Analytics
    ####################################################################

    def export_feature_analytics(
        self,
    ) -> dict[str, Any]:
        """
        Exports complete feature analytics.
        """

        return {
            "feature_statistics":
                self.calculate_feature_statistics(),
            "top_features":
                self.top_features(),
            "least_used_features":
                self.least_used_features(),
            "feature_adoption":
                self.feature_adoption(),
            "most_successful_features":
                self.most_successful_features(),
            "most_failure_prone_features":
                self.most_failure_prone_features(),
        }

    ####################################################################
    # Export - Customer Analytics
    ####################################################################

    def export_customer_analytics(
        self,
    ) -> dict[str, Any]:
        """
        Exports customer analytics.
        """

        return {
            "customer_distribution":
                self.customer_distribution(),
            "power_users":
                self.power_users(),
        }

    ####################################################################
    # Export - Workflow Analytics
    ####################################################################

    def export_workflow_analytics(
        self,
    ) -> dict[str, Any]:
        """
        Exports workflow analytics.
        """

        return {
            "workflow_distribution":
                self.workflow_distribution(),
        }

    ####################################################################
    # Export - Trend Analytics
    ####################################################################

    def export_trend_analytics(
        self,
    ) -> dict[str, Any]:
        """
        Exports trend analytics.
        """

        return {
            "hourly_usage":
                self.hourly_usage(),
            "daily_usage":
                self.daily_usage(),
            "weekly_usage":
                self.weekly_usage(),
            "monthly_usage":
                self.monthly_usage(),
            "trend_summary":
                self.trend_summary(),
        }

    ####################################################################
    # Dashboard Summary
    ####################################################################

    def analytics_dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a lightweight dashboard summary.
        """

        summary = self.feature_usage_summary()

        summary["top_features"] = self.top_features(5)

        summary["power_users"] = self.power_users(5)

        summary["peak_hour"] = self.peak_usage_hour()

        summary["peak_day"] = self.peak_usage_day()

        return summary

    ####################################################################
    # Export Everything
    ####################################################################

    def export_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Exports complete analytics.
        """

        logger.info(
            "Exporting complete analytics."
        )

        return {
            "summary":
                self.feature_usage_summary(),

            "feature_analytics":
                self.export_feature_analytics(),

            "customer_analytics":
                self.export_customer_analytics(),

            "workflow_analytics":
                self.export_workflow_analytics(),

            "trend_analytics":
                self.export_trend_analytics(),

            "dashboard":
                self.analytics_dashboard_summary(),
        }

    ####################################################################
    # Convenience Methods
    ####################################################################

    def total_customers(
        self,
    ) -> int:
        """
        Returns total customers.
        """

        return len(
            self.customer_distribution()
        )

    def total_features(
        self,
    ) -> int:
        """
        Returns total tracked features.
        """

        return len(
            self.calculate_feature_statistics()
        )

    def total_sessions(
        self,
    ) -> int:
        """
        Returns total sessions.
        """

        events = self._collect_events()

        return len(
            {
                event.session_id
                for event in events
            }
        )

    def total_usage_events(
        self,
    ) -> int:
        """
        Returns total usage events.
        """

        return len(
            self._collect_events()
        )

    ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:
        """
        Returns analytics engine health information.
        """

        return {
            "status": "healthy",
            "events": self.total_usage_events(),
            "customers": self.total_customers(),
            "features": self.total_features(),
            "sessions": self.total_sessions(),
        }
