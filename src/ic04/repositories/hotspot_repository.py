"""
hotspot_repository.py

Repository for storing runtime hotspots.
"""

from typing import Dict, List, Optional

from src.ic04.models.hotspot import Hotspot


class HotspotRepository:
    """
    Stores identified runtime hotspots.
    """

    def __init__(self):
        self._hotspots: Dict[str, Hotspot] = {}

    def add_hotspot(self, hotspot: Hotspot):
        """
        Store a hotspot.
        """
        self._hotspots[hotspot.method_name] = hotspot

    def get_hotspot(self, method_name: str) -> Optional[Hotspot]:
        """
        Retrieve hotspot for a method.
        """
        return self._hotspots.get(method_name)

    def get_all_hotspots(self) -> List[Hotspot]:
        """
        Return all hotspots.
        """
        return list(self._hotspots.values())

    def get_hotspots_by_level(
        self,
        level: str
    ) -> List[Hotspot]:
        """
        Return hotspots matching a severity level.
        """
        return [
            hotspot
            for hotspot in self._hotspots.values()
            if hotspot.hotspot_level == level
        ]

    def get_sorted_hotspots(
        self,
        descending: bool = True
    ) -> List[Hotspot]:
        """
        Return hotspots sorted by average execution time.
        """
        return sorted(
            self._hotspots.values(),
            key=lambda hotspot: hotspot.average_time,
            reverse=descending,
        )

    def clear(self):
        """
        Remove all hotspots.
        """
        self._hotspots.clear()

    def size(self):
        """
        Number of hotspots.
        """
        return len(self._hotspots)

    def __len__(self):
        return len(self._hotspots)

    def __iter__(self):
        return iter(self._hotspots.values())

    def __contains__(self, method_name):
        return method_name in self._hotspots

    def __str__(self):
        return (
            f"HotspotRepository("
            f"hotspots={len(self._hotspots)})"
        )
