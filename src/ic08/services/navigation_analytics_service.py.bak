from __future__ import annotations

import logging
from collections import Counter
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)

logger = logging.getLogger(__name__)


class NavigationAnalyticsService:
    """
    Provides navigation analytics for customer journeys.

    Responsibilities:
        - Collect navigation paths
        - Analyze page transitions
        - Entry/Exit analysis
        - Navigation depth
        - Bounce analysis
        - Navigation dashboard
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(
        self,
        journey_builder: CustomerJourneyBuilder,
    ) -> None:
        """
        Initializes the Navigation Analytics Service.
        """

        self._journey_builder = journey_builder

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
            "Collected %d journeys.",
            len(journeys),
        )

        return journeys

    ####################################################################
    # Navigation Collection
    ####################################################################

    def _navigation_paths(
        self,
    ) -> list[list[str]]:
        """
        Returns all navigation paths.
        """

        return [
            journey["navigation_path"]
            for journey in self._collect_journeys()
            if journey["navigation_path"]
        ]

    def _entry_pages(
        self,
    ) -> list[str]:
        """
        Returns all entry pages.
        """

        return [
            journey["entry_page"]
            for journey in self._collect_journeys()
            if journey["entry_page"]
        ]

    def _exit_pages(
        self,
    ) -> list[str]:
        """
        Returns all exit pages.
        """

        return [
            journey["exit_page"]
            for journey in self._collect_journeys()
            if journey["exit_page"]
        ]

    def _transition_pairs(
        self,
    ) -> list[tuple[str, str]]:
        """
        Returns page transition pairs.

        Example:
            Home -> Search -> Product

        Returns:
            (Home, Search)
            (Search, Product)
        """

        transitions: list[tuple[str, str]] = []

        for path in self._navigation_paths():

            transitions.extend(
                zip(
                    path[:-1],
                    path[1:],
                )
            )

        return transitions

    def _page_visits(
        self,
    ) -> Counter[str]:
        """
        Returns page visit counts.
        """

        counter: Counter[str] = Counter()

        for path in self._navigation_paths():
            counter.update(path)

        return counter


         ####################################################################
    # Page Analytics
    ####################################################################

    def page_visit_counts(
        self,
    ) -> dict[str, int]:
        """
        Returns the number of visits for every page.
        """

        return dict(self._page_visits())

    def page_popularity(
        self,
    ) -> list[tuple[str, int]]:
        """
        Returns pages sorted by popularity.
        """

        return self._page_visits().most_common()

    def most_visited_pages(
        self,
        top_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the most visited pages.
        """

        return self._page_visits().most_common(top_n)

    def least_visited_pages(
        self,
        bottom_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the least visited pages.
        """

        visits = sorted(
            self._page_visits().items(),
            key=lambda item: item[1],
        )

        return visits[:bottom_n]

    def unique_pages(
        self,
    ) -> list[str]:
        """
        Returns all unique pages.
        """

        return sorted(
            self._page_visits().keys()
        )

    def total_unique_pages(
        self,
    ) -> int:
        """
        Returns the total number of unique pages.
        """

        return len(
            self._page_visits()
        )

    def total_page_visits(
        self,
    ) -> int:
        """
        Returns the total number of page visits.
        """

        return sum(
            self._page_visits().values()
        )

    def average_pages_per_journey(
        self,
    ) -> float:
        """
        Returns the average number of pages visited per journey.
        """

        journeys = self._collect_journeys()

        if not journeys:
            return 0.0

        return round(
            sum(
                len(journey["navigation_path"])
                for journey in journeys
            )
            / len(journeys),
            2,
        )

    def page_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns overall page analytics.
        """

        return {
            "total_unique_pages": self.total_unique_pages(),
            "total_page_visits": self.total_page_visits(),
            "average_pages_per_journey": self.average_pages_per_journey(),
            "most_visited_pages": self.most_visited_pages(10),
            "least_visited_pages": self.least_visited_pages(10),
        }

    def page_exists(
        self,
        page_name: str,
    ) -> bool:
        """
        Returns True if the page exists.
        """

        return page_name in self._page_visits()

    def page_visit_count(
        self,
        page_name: str,
    ) -> int:
        """
        Returns the number of visits for a page.
        """

        return self._page_visits().get(
            page_name,
            0,
        )

         ####################################################################
    # Navigation Flow Analytics
    ####################################################################

    def transition_counts(
        self,
    ) -> dict[tuple[str, str], int]:
        """
        Returns the number of occurrences of each page transition.
        """

        return dict(
            Counter(
                self._transition_pairs()
            )
        )

    def most_common_transitions(
        self,
        top_n: int = 10,
    ) -> list[tuple[tuple[str, str], int]]:
        """
        Returns the most common page transitions.
        """

        return Counter(
            self._transition_pairs()
        ).most_common(top_n)

    def transition_matrix(
        self,
    ) -> dict[str, dict[str, int]]:
        """
        Builds a transition matrix.

        {
            "Home": {
                "Search": 25,
                "Profile": 12,
            }
        }
        """

        matrix: dict[str, dict[str, int]] = {}

        for source, destination in self._transition_pairs():

            matrix.setdefault(source, {})
            matrix[source][destination] = (
                matrix[source].get(destination, 0)
                + 1
            )

        return matrix

    def common_navigation_paths(
        self,
        top_n: int = 10,
    ) -> list[tuple[tuple[str, ...], int]]:
        """
        Returns the most common navigation paths.
        """

        counter = Counter(
            tuple(path)
            for path in self._navigation_paths()
        )

        return counter.most_common(top_n)

    def longest_navigation_path(
        self,
    ) -> list[str]:
        """
        Returns the longest navigation path.
        """

        paths = self._navigation_paths()

        if not paths:
            return []

        return max(
            paths,
            key=len,
        )

    def shortest_navigation_path(
        self,
    ) -> list[str]:
        """
        Returns the shortest navigation path.
        """

        paths = self._navigation_paths()

        if not paths:
            return []

        return min(
            paths,
            key=len,
        )

    def average_navigation_depth(
        self,
    ) -> float:
        """
        Returns the average navigation depth.
        """

        paths = self._navigation_paths()

        if not paths:
            return 0.0

        return round(
            sum(
                len(path)
                for path in paths
            )
            / len(paths),
            2,
        )

    def navigation_depth_distribution(
        self,
    ) -> dict[int, int]:
        """
        Returns the distribution of navigation depths.
        """

        distribution: Counter[int] = Counter()

        for path in self._navigation_paths():
            distribution[len(path)] += 1

        return dict(distribution)

    def navigation_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns navigation flow statistics.
        """

        return {
            "average_navigation_depth":
                self.average_navigation_depth(),
            "longest_navigation_path":
                self.longest_navigation_path(),
            "shortest_navigation_path":
                self.shortest_navigation_path(),
            "most_common_transitions":
                self.most_common_transitions(),
            "common_navigation_paths":
                self.common_navigation_paths(),
        }

         ####################################################################
    # Entry & Exit Analytics
    ####################################################################

    def entry_page_counts(
        self,
    ) -> dict[str, int]:
        """
        Returns the number of sessions starting on each page.
        """

        return dict(
            Counter(
                self._entry_pages()
            )
        )

    def exit_page_counts(
        self,
    ) -> dict[str, int]:
        """
        Returns the number of sessions ending on each page.
        """

        return dict(
            Counter(
                self._exit_pages()
            )
        )

    def most_common_entry_pages(
        self,
        top_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the most common entry pages.
        """

        return Counter(
            self._entry_pages()
        ).most_common(top_n)

    def most_common_exit_pages(
        self,
        top_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the most common exit pages.
        """

        return Counter(
            self._exit_pages()
        ).most_common(top_n)

    def entry_exit_pairs(
        self,
    ) -> list[tuple[str, str]]:
        """
        Returns entry and exit page pairs for every journey.
        """

        return [
            (
                journey["entry_page"],
                journey["exit_page"],
            )
            for journey in self._collect_journeys()
            if journey["entry_page"]
            and journey["exit_page"]
        ]

    def most_common_entry_exit_pairs(
        self,
        top_n: int = 10,
    ) -> list[tuple[tuple[str, str], int]]:
        """
        Returns the most common entry/exit combinations.
        """

        return Counter(
            self.entry_exit_pairs()
        ).most_common(top_n)

    def entry_exit_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns summary statistics for entry and exit pages.
        """

        return {
            "entry_page_counts":
                self.entry_page_counts(),
            "exit_page_counts":
                self.exit_page_counts(),
            "most_common_entry_pages":
                self.most_common_entry_pages(),
            "most_common_exit_pages":
                self.most_common_exit_pages(),
            "most_common_entry_exit_pairs":
                self.most_common_entry_exit_pairs(),
        }

    def entry_page_exists(
        self,
        page_name: str,
    ) -> bool:
        """
        Returns True if the page has been used as an entry page.
        """

        return page_name in self.entry_page_counts()

    def exit_page_exists(
        self,
        page_name: str,
    ) -> bool:
        """
        Returns True if the page has been used as an exit page.
        """

        return page_name in self.exit_page_counts()



         ####################################################################
    # Bounce & Drop-off Analytics
    ####################################################################

    def bounce_journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns journeys containing only a single page visit.
        """

        return [
            journey
            for journey in self._collect_journeys()
            if len(journey["navigation_path"]) <= 1
        ]

    def bounce_rate(
        self,
    ) -> float:
        """
        Returns the percentage of bounced journeys.
        """

        journeys = self._collect_journeys()

        if not journeys:
            return 0.0

        return round(
            len(self.bounce_journeys()) * 100
            / len(journeys),
            2,
        )

    def dead_end_pages(
        self,
    ) -> list[str]:
        """
        Returns pages that appear only as exit pages.
        """

        entry_pages = set(
            self._entry_pages()
        )

        exit_pages = set(
            self._exit_pages()
        )

        return sorted(
            exit_pages - entry_pages
        )

    def orphan_pages(
        self,
    ) -> list[str]:
        """
        Returns pages that have no incoming or outgoing transitions.
        """

        transitions = self._transition_pairs()

        connected = set()

        for source, destination in transitions:
            connected.add(source)
            connected.add(destination)

        all_pages = set(
            self.unique_pages()
        )

        return sorted(
            all_pages - connected
        )

    def navigation_dropoffs(
        self,
    ) -> dict[str, int]:
        """
        Counts how often each page is the final page in a journey.
        """

        return dict(
            Counter(
                self._exit_pages()
            )
        )

    def highest_dropoff_pages(
        self,
        top_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns pages with the highest number of drop-offs.
        """

        return Counter(
            self._exit_pages()
        ).most_common(top_n)

    def single_page_sessions(
        self,
    ) -> int:
        """
        Returns the number of single-page sessions.
        """

        return len(
            self.bounce_journeys()
        )

    def multi_page_sessions(
        self,
    ) -> int:
        """
        Returns the number of multi-page sessions.
        """

        return len(
            self._collect_journeys()
        ) - self.single_page_sessions()

    def bounce_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns bounce and drop-off analytics.
        """

        return {
            "bounce_rate": self.bounce_rate(),
            "single_page_sessions": self.single_page_sessions(),
            "multi_page_sessions": self.multi_page_sessions(),
            "dead_end_pages": self.dead_end_pages(),
            "orphan_pages": self.orphan_pages(),
            "highest_dropoff_pages": self.highest_dropoff_pages(),
        }


         ####################################################################
    # Dashboard & Reporting
    ####################################################################

    def dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a dashboard summary for navigation analytics.
        """

        return {
            "total_journeys": len(self._collect_journeys()),
            "total_unique_pages": self.total_unique_pages(),
            "total_page_visits": self.total_page_visits(),
            "average_navigation_depth": self.average_navigation_depth(),
            "bounce_rate": self.bounce_rate(),
            "most_visited_pages": self.most_visited_pages(5),
            "most_common_transitions": self.most_common_transitions(5),
            "most_common_entry_pages": self.most_common_entry_pages(5),
            "most_common_exit_pages": self.most_common_exit_pages(5),
            "highest_dropoff_pages": self.highest_dropoff_pages(5),
        }

    ####################################################################
    # Export APIs
    ####################################################################

    def export_navigation_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Exports complete navigation analytics.
        """

        return {
            "page_statistics": self.page_statistics(),
            "navigation_statistics": self.navigation_statistics(),
            "entry_exit_statistics": self.entry_exit_statistics(),
            "bounce_statistics": self.bounce_statistics(),
            "dashboard": self.dashboard_summary(),
        }

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
            "service": "NavigationAnalyticsService",
            "journeys_processed": len(journeys),
            "unique_pages": self.total_unique_pages(),
            "page_visits": self.total_page_visits(),
            "transitions": len(self._transition_pairs()),
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
            "service": "NavigationAnalyticsService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
            "supported_operations": [
                "Page Analytics",
                "Navigation Flow Analytics",
                "Entry Analytics",
                "Exit Analytics",
                "Bounce Analytics",
                "Drop-off Analytics",
                "Dashboard Summary",
                "Export Navigation Statistics",
                "Health Check",
            ],
        }
