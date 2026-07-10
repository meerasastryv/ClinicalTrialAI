"""
hotspot_analyzer.py

Analyzes runtime performance metrics and identifies
performance hotspots.
"""

from src.ic04.models.hotspot import Hotspot
from src.ic04.repositories.hotspot_repository import HotspotRepository


class HotspotAnalyzer:
    """
    Identifies runtime hotspots from performance metrics.
    """

    HIGH_THRESHOLD = 1.0      # milliseconds
    MEDIUM_THRESHOLD = 0.1    # milliseconds

    def __init__(self):
        self.hotspot_repository = HotspotRepository()

    def analyze(self, performance_repository):
        """
        Analyze performance metrics and classify hotspots.
        """

        self.hotspot_repository.clear()

        metrics = performance_repository.get_all_metrics()

        for metric in metrics:

            hotspot = Hotspot(
                method_name=metric.method_name,
                call_count=metric.call_count,
                average_time=metric.average_time,
                total_time=metric.total_time,
                hotspot_level=self._determine_level(
                    metric.average_time
                ),
            )

            self.hotspot_repository.add_hotspot(hotspot)

        return self.hotspot_repository

    def _determine_level(self, average_time):
        """
        Determine hotspot severity.
        """

        if average_time >= self.HIGH_THRESHOLD:
            return "HIGH"

        if average_time >= self.MEDIUM_THRESHOLD:
            return "MEDIUM"

        return "LOW"

    def get_repository(self):
        """
        Return hotspot repository.
        """
        return self.hotspot_repository

    def get_high_hotspots(self):
        return self.hotspot_repository.get_hotspots_by_level("HIGH")

    def get_medium_hotspots(self):
        return self.hotspot_repository.get_hotspots_by_level("MEDIUM")

    def get_low_hotspots(self):
        return self.hotspot_repository.get_hotspots_by_level("LOW")

    def get_summary(self):
        """
        Return hotspot statistics.
        """

        return {
            "total_hotspots": self.hotspot_repository.size(),
            "high": len(self.get_high_hotspots()),
            "medium": len(self.get_medium_hotspots()),
            "low": len(self.get_low_hotspots()),
        }

    def clear(self):
        self.hotspot_repository.clear()
