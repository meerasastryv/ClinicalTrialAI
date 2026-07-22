from __future__ import annotations

import logging
from collections import Counter
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)
from src.ic08.services.navigation_analytics_service import (
    NavigationAnalyticsService,
)

logger = logging.getLogger(__name__)


class FunnelAnalysisService:
    """
    Provides funnel analytics for customer journeys.
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(
        self,
        journey_builder: CustomerJourneyBuilder,
        navigation_service: NavigationAnalyticsService,
    ) -> None:
        """
        Initializes the Funnel Analysis Service.
        """

        self._journey_builder = journey_builder
        self._navigation_service = navigation_service

    ####################################################################
    # Journey Collection
    ####################################################################

    def _collect_journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns all customer journeys.
        """

        journeys = self._journey_builder.build_all_journeys()

        logger.debug(
            "Collected %d journeys for funnel analysis.",
            len(journeys),
        )

        return journeys

    ####################################################################
    # Funnel Helpers
    ####################################################################

    def _validate_funnel(
        self,
        funnel: list[str],
    ) -> bool:
        """
        Validates a funnel definition.
        """

        return len(funnel) > 0

    def _stage_names(
        self,
        funnel: list[str],
    ) -> list[str]:
        """
        Returns funnel stage names.
        """

        return funnel.copy()

    def _stage_counts(
        self,
        funnel: list[str],
    ) -> dict[str, int]:
        """
        Initializes stage counters.
        """

        return {
            stage: 0
            for stage in funnel
        }

    def _journey_contains_stage(
        self,
        journey: dict[str, Any],
        stage: str,
    ) -> bool:
        """
        Returns True if the journey contains the stage.
        """

        return stage in journey["navigation_path"]

    def _journey_stage_index(
        self,
        journey: dict[str, Any],
        stage: str,
    ) -> int:
        """
        Returns the index of the stage within the journey.
        Returns -1 if the stage does not exist.
        """

        try:
            return journey["navigation_path"].index(stage)
        except ValueError:
            return -1


         ####################################################################
    # Funnel Progression
    ####################################################################

    def journeys_entering_funnel(
        self,
        funnel: list[str],
    ) -> list[dict[str, Any]]:
        """
        Returns journeys that entered the funnel.
        """

        if not self._validate_funnel(funnel):
            return []

        first_stage = funnel[0]

        return [
            journey
            for journey in self._collect_journeys()
            if self._journey_contains_stage(
                journey,
                first_stage,
            )
        ]

    def journeys_reaching_stage(
        self,
        funnel: list[str],
        stage: str,
    ) -> list[dict[str, Any]]:
        """
        Returns journeys that reached the specified stage.
        """

        if stage not in funnel:
            return []

        return [
            journey
            for journey in self.journeys_entering_funnel(
                funnel,
            )
            if self._journey_contains_stage(
                journey,
                stage,
            )
        ]

    def journeys_completing_funnel(
        self,
        funnel: list[str],
    ) -> list[dict[str, Any]]:
        """
        Returns journeys that completed every stage of the funnel
        in the correct order.
        """

        completed = []

        for journey in self.journeys_entering_funnel(
            funnel,
        ):

            previous_index = -1
            success = True

            for stage in funnel:

                index = self._journey_stage_index(
                    journey,
                    stage,
                )

                if index == -1 or index < previous_index:
                    success = False
                    break

                previous_index = index

            if success:
                completed.append(journey)

        return completed

    def journeys_abandoning_stage(
        self,
        funnel: list[str],
        stage: str,
    ) -> list[dict[str, Any]]:
        """
        Returns journeys that reached a stage but did not
        proceed to the next stage.
        """

        if stage not in funnel:
            return []

        stage_index = funnel.index(stage)

        if stage_index == len(funnel) - 1:
            return []

        next_stage = funnel[stage_index + 1]

        abandoned = []

        for journey in self.journeys_reaching_stage(
            funnel,
            stage,
        ):

            if not self._journey_contains_stage(
                journey,
                next_stage,
            ):
                abandoned.append(journey)

        return abandoned

    def stage_completion_counts(
        self,
        funnel: list[str],
    ) -> dict[str, int]:
        """
        Returns the number of journeys reaching each stage.
        """

        counts = self._stage_counts(funnel)

        for stage in funnel:

            counts[stage] = len(
                self.journeys_reaching_stage(
                    funnel,
                    stage,
                )
            )

        return counts

    def stage_completion_percentage(
        self,
        funnel: list[str],
    ) -> dict[str, float]:
        """
        Returns completion percentage for each stage.
        """

        entered = len(
            self.journeys_entering_funnel(
                funnel,
            )
        )

        if entered == 0:
            return {
                stage: 0.0
                for stage in funnel
            }

        percentages = {}

        for stage, count in (
            self.stage_completion_counts(
                funnel,
            ).items()
        ):

            percentages[stage] = round(
                count * 100 / entered,
                2,
            )

        return percentages


         ####################################################################
    # Conversion Analytics
    ####################################################################

    def conversion_rate(
        self,
        funnel: list[str],
        stage: str,
    ) -> float:
        """
        Returns the conversion percentage for a specific stage.
        """

        if stage not in funnel:
            return 0.0

        entered = len(
            self.journeys_entering_funnel(
                funnel,
            )
        )

        if entered == 0:
            return 0.0

        reached = len(
            self.journeys_reaching_stage(
                funnel,
                stage,
            )
        )

        return round(
            reached * 100 / entered,
            2,
        )

    def overall_conversion_rate(
        self,
        funnel: list[str],
    ) -> float:
        """
        Returns the overall funnel conversion percentage.
        """

        entered = len(
            self.journeys_entering_funnel(
                funnel,
            )
        )

        if entered == 0:
            return 0.0

        completed = len(
            self.journeys_completing_funnel(
                funnel,
            )
        )

        return round(
            completed * 100 / entered,
            2,
        )

    def stage_conversion_rates(
        self,
        funnel: list[str],
    ) -> dict[str, float]:
        """
        Returns conversion percentage for every stage.
        """

        return {
            stage: self.conversion_rate(
                funnel,
                stage,
            )
            for stage in funnel
        }

    def best_converting_stage(
        self,
        funnel: list[str],
    ) -> tuple[str, float] | None:
        """
        Returns the stage with the highest conversion rate.
        """

        rates = self.stage_conversion_rates(
            funnel,
        )

        if not rates:
            return None

        return max(
            rates.items(),
            key=lambda item: item[1],
        )

    def lowest_converting_stage(
        self,
        funnel: list[str],
    ) -> tuple[str, float] | None:
        """
        Returns the stage with the lowest conversion rate.
        """

        rates = self.stage_conversion_rates(
            funnel,
        )

        if not rates:
            return None

        return min(
            rates.items(),
            key=lambda item: item[1],
        )

    def stage_to_stage_conversion(
        self,
        funnel: list[str],
    ) -> dict[str, float]:
        """
        Returns conversion percentages between consecutive stages.
        """

        counts = self.stage_completion_counts(
            funnel,
        )

        conversions: dict[str, float] = {}

        for index in range(len(funnel) - 1):

            current_stage = funnel[index]
            next_stage = funnel[index + 1]

            current_count = counts[current_stage]
            next_count = counts[next_stage]

            if current_count == 0:
                conversions[
                    f"{current_stage} -> {next_stage}"
                ] = 0.0
            else:
                conversions[
                    f"{current_stage} -> {next_stage}"
                ] = round(
                    next_count * 100 / current_count,
                    2,
                )

        return conversions

    def conversion_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns overall conversion analytics.
        """

        return {
            "overall_conversion_rate":
                self.overall_conversion_rate(
                    funnel,
                ),
            "stage_conversion_rates":
                self.stage_conversion_rates(
                    funnel,
                ),
            "stage_to_stage_conversion":
                self.stage_to_stage_conversion(
                    funnel,
                ),
            "best_converting_stage":
                self.best_converting_stage(
                    funnel,
                ),
            "lowest_converting_stage":
                self.lowest_converting_stage(
                    funnel,
                ),
        }


         ####################################################################
    # Drop-off Analytics
    ####################################################################

    def dropoff_counts(
        self,
        funnel: list[str],
    ) -> dict[str, int]:
        """
        Returns the number of journeys that abandoned after each stage.
        """

        counts = self._stage_counts(funnel)

        for stage in funnel[:-1]:
            counts[stage] = len(
                self.journeys_abandoning_stage(
                    funnel,
                    stage,
                )
            )

        counts[funnel[-1]] = 0

        return counts

    def dropoff_rate(
        self,
        funnel: list[str],
        stage: str,
    ) -> float:
        """
        Returns the drop-off percentage for a stage.
        """

        if stage not in funnel:
            return 0.0

        reached = len(
            self.journeys_reaching_stage(
                funnel,
                stage,
            )
        )

        if reached == 0:
            return 0.0

        abandoned = len(
            self.journeys_abandoning_stage(
                funnel,
                stage,
            )
        )

        return round(
            abandoned * 100 / reached,
            2,
        )

    def stage_dropoff_rates(
        self,
        funnel: list[str],
    ) -> dict[str, float]:
        """
        Returns drop-off percentage for every stage.
        """

        return {
            stage: self.dropoff_rate(
                funnel,
                stage,
            )
            for stage in funnel[:-1]
        }

    def highest_dropoff_stage(
        self,
        funnel: list[str],
    ) -> tuple[str, float] | None:
        """
        Returns the stage with the highest drop-off rate.
        """

        rates = self.stage_dropoff_rates(
            funnel,
        )

        if not rates:
            return None

        return max(
            rates.items(),
            key=lambda item: item[1],
        )

    def lowest_dropoff_stage(
        self,
        funnel: list[str],
    ) -> tuple[str, float] | None:
        """
        Returns the stage with the lowest drop-off rate.
        """

        rates = self.stage_dropoff_rates(
            funnel,
        )

        if not rates:
            return None

        return min(
            rates.items(),
            key=lambda item: item[1],
        )

    def stage_retention_rates(
        self,
        funnel: list[str],
    ) -> dict[str, float]:
        """
        Returns retention percentage for every stage.
        """

        return {
            stage: round(
                100.0 - self.dropoff_rate(
                    funnel,
                    stage,
                ),
                2,
            )
            for stage in funnel[:-1]
        }

    def dropoff_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns overall drop-off analytics.
        """

        return {
            "dropoff_counts":
                self.dropoff_counts(
                    funnel,
                ),
            "stage_dropoff_rates":
                self.stage_dropoff_rates(
                    funnel,
                ),
            "stage_retention_rates":
                self.stage_retention_rates(
                    funnel,
                ),
            "highest_dropoff_stage":
                self.highest_dropoff_stage(
                    funnel,
                ),
            "lowest_dropoff_stage":
                self.lowest_dropoff_stage(
                    funnel,
                ),
        }


         ####################################################################
    # Dashboard & Export
    ####################################################################

    def funnel_summary(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns a comprehensive summary of funnel analytics.
        """

        return {
            "funnel": funnel,
            "journeys_entering": len(
                self.journeys_entering_funnel(
                    funnel,
                )
            ),
            "journeys_completed": len(
                self.journeys_completing_funnel(
                    funnel,
                )
            ),
            "overall_conversion_rate":
                self.overall_conversion_rate(
                    funnel,
                ),
            "stage_completion_counts":
                self.stage_completion_counts(
                    funnel,
                ),
            "stage_completion_percentage":
                self.stage_completion_percentage(
                    funnel,
                ),
            "stage_conversion_rates":
                self.stage_conversion_rates(
                    funnel,
                ),
            "stage_dropoff_rates":
                self.stage_dropoff_rates(
                    funnel,
                ),
            "stage_retention_rates":
                self.stage_retention_rates(
                    funnel,
                ),
        }

    def dashboard_summary(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns dashboard information for the funnel.
        """

        return {
            "overall_conversion_rate":
                self.overall_conversion_rate(
                    funnel,
                ),
            "best_converting_stage":
                self.best_converting_stage(
                    funnel,
                ),
            "lowest_converting_stage":
                self.lowest_converting_stage(
                    funnel,
                ),
            "highest_dropoff_stage":
                self.highest_dropoff_stage(
                    funnel,
                ),
            "lowest_dropoff_stage":
                self.lowest_dropoff_stage(
                    funnel,
                ),
        }

    ####################################################################
    # Export APIs
    ####################################################################

    def export_funnel(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Exports complete funnel analytics.
        """

        return {
            "summary":
                self.funnel_summary(
                    funnel,
                ),
            "conversion_statistics":
                self.conversion_statistics(
                    funnel,
                ),
            "dropoff_statistics":
                self.dropoff_statistics(
                    funnel,
                ),
            "dashboard":
                self.dashboard_summary(
                    funnel,
                ),
        }

    ####################################################################
    # Search Utilities
    ####################################################################

    def funnel_exists(
        self,
        funnel: list[str],
    ) -> bool:
        """
        Returns True if the funnel is valid.
        """

        return self._validate_funnel(
            funnel,
        )

    def total_funnel_stages(
        self,
        funnel: list[str],
    ) -> int:
        """
        Returns the number of stages in the funnel.
        """

        return len(funnel)

    def completed_funnel_percentage(
        self,
        funnel: list[str],
    ) -> float:
        """
        Alias for the overall funnel conversion percentage.
        """

        return self.overall_conversion_rate(
            funnel,
        )



         ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:
        """
        Returns service health information.
        """

        journeys = self._collect_journeys()

        return {
            "status": "healthy",
            "service": "FunnelAnalysisService",
            "journeys_processed": len(journeys),
            "navigation_paths": len(
                self._navigation_service._navigation_paths()
            ),
        }

    ####################################################################
    # Service Information
    ####################################################################

    def service_information(
        self,
    ) -> dict[str, Any]:
        """
        Returns metadata about the service.
        """

        return {
            "service": "FunnelAnalysisService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
            "supported_operations": [
                "Funnel Progression",
                "Stage Completion",
                "Conversion Analytics",
                "Drop-off Analytics",
                "Retention Analytics",
                "Dashboard Summary",
                "Export Funnel Analytics",
                "Health Check",
            ],
        }

    ####################################################################
    # Readiness
    ####################################################################

    def is_ready(
        self,
    ) -> bool:
        """
        Returns True if the service is ready for analysis.
        """

        return self.health_check()["status"] == "healthy"

    def total_journeys(
        self,
    ) -> int:
        """
        Returns the number of journeys available for analysis.
        """

        return len(
            self._collect_journeys()
        )

    def service_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a high-level service summary.
        """

        return {
            "service": "FunnelAnalysisService",
            "ready": self.is_ready(),
            "total_journeys": self.total_journeys(),
            "health": self.health_check(),
        }
