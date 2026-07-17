"""
search_repository.py

IC-07 - Test Data Intelligence Engine
Milestone 8 - Intelligent Test Data Search

Repository for storing and managing SearchResult objects.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

from src.ic07.models.search_result import SearchResult


class SearchRepository:
    """
    Repository for SearchResult objects.
    """

    def __init__(self) -> None:
        self._results: Dict[str, SearchResult] = {}

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def add(self, result: SearchResult) -> None:
        """
        Add or replace a search result.
        """
        self._results[result.dataset_name] = result

    def get(self, dataset_name: str) -> Optional[SearchResult]:
        """
        Retrieve a search result by dataset name.
        """
        return self._results.get(dataset_name)

    def remove(self, dataset_name: str) -> bool:
        """
        Remove a search result.
        """
        return self._results.pop(dataset_name, None) is not None

    def clear(self) -> None:
        """
        Remove all search results.
        """
        self._results.clear()

    # ------------------------------------------------------------------
    # Query Operations
    # ------------------------------------------------------------------

    def exists(self, dataset_name: str) -> bool:
        """
        Check whether a result exists.
        """
        return dataset_name in self._results

    def count(self) -> int:
        """
        Number of stored results.
        """
        return len(self._results)

    def list_all(self) -> List[SearchResult]:
        """
        Return all search results.
        """
        return list(self._results.values())

    def top(self, limit: int = 10) -> List[SearchResult]:
        """
        Return highest scored search results.
        """
        return sorted(
            self._results.values(),
            key=lambda r: r.score,
            reverse=True,
        )[:limit]

    def search(self, keyword: str) -> List[SearchResult]:
        """
        Search by dataset name or matched keywords.
        """
        keyword = keyword.lower()

        results = []

        for result in self._results.values():

            if keyword in result.dataset_name.lower():
                results.append(result)
                continue

            if any(
                keyword in value.lower()
                for value in result.matched_keywords
            ):
                results.append(result)

        return results

    # ------------------------------------------------------------------
    # Ranking
    # ------------------------------------------------------------------

    def rank(self) -> List[SearchResult]:
        """
        Assign ranks based on score.
        """
        ranked = sorted(
            self._results.values(),
            key=lambda r: r.score,
            reverse=True,
        )

        for index, result in enumerate(ranked, start=1):
            result.rank = index

        return ranked

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, file_path: str) -> None:
        """
        Save search results to JSON.
        """
        data = [
            result.to_dict()
            for result in self.rank()
        ]

        Path(file_path).write_text(
            json.dumps(data, indent=4),
            encoding="utf-8",
        )

    def load(self, file_path: str) -> None:
        """
        Load search results from JSON.
        """
        path = Path(file_path)

        if not path.exists():
            return

        records = json.loads(
            path.read_text(encoding="utf-8")
        )

        self.clear()

        for record in records:
            self.add(SearchResult.from_dict(record))

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def average_score(self) -> float:
        """
        Calculate average score.
        """
        if not self._results:
            return 0.0

        return (
            sum(result.score for result in self._results.values())
            / len(self._results)
        )

    def highest_score(self) -> float:
        """
        Return highest score.
        """
        if not self._results:
            return 0.0

        return max(
            result.score
            for result in self._results.values()
        )

    def lowest_score(self) -> float:
        """
        Return lowest score.
        """
        if not self._results:
            return 0.0

        return min(
            result.score
            for result in self._results.values()
        )

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return self.count()

    def __iter__(self):
        return iter(self.rank())

    def __contains__(self, dataset_name: str) -> bool:
        return self.exists(dataset_name)
