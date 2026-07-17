"""
IC-07 Test Data Repository

Provides repository operations for TestData objects.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional

from src.ic07.models.test_data import TestData


logger = logging.getLogger(__name__)


class TestDataRepository:
    """
    Repository for managing TestData objects.
    """

    def __init__(self) -> None:
        self._repository: Dict[str, TestData] = {}

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def add(self, test_data: TestData) -> None:
        """
        Add or update a TestData object.
        """
        self._repository[test_data.data_id] = test_data
        logger.info("Stored TestData: %s", test_data.data_id)

    def get(self, data_id: str) -> Optional[TestData]:
        """
        Retrieve a TestData object by ID.
        """
        return self._repository.get(data_id)

    def update(self, test_data: TestData) -> None:
        """
        Update an existing TestData object.
        """
        self._repository[test_data.data_id] = test_data
        logger.info("Updated TestData: %s", test_data.data_id)

    def delete(self, data_id: str) -> bool:
        """
        Delete a TestData object.
        """
        if data_id in self._repository:
            del self._repository[data_id]
            logger.info("Deleted TestData: %s", data_id)
            return True

        return False

    # ------------------------------------------------------------------
    # Retrieval
    # ------------------------------------------------------------------

    def get_all(self) -> List[TestData]:
        """
        Return all TestData objects.
        """
        return list(self._repository.values())

    def exists(self, data_id: str) -> bool:
        """
        Check whether a record exists.
        """
        return data_id in self._repository

    def count(self) -> int:
        """
        Return repository size.
        """
        return len(self._repository)

    def clear(self) -> None:
        """
        Remove all records.
        """
        self._repository.clear()
        logger.info("Repository cleared.")

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_dataset(self, dataset_name: str) -> List[TestData]:
        """
        Find records by dataset.
        """
        return [
            record
            for record in self._repository.values()
            if record.dataset_name == dataset_name
        ]

    def find_by_category(self, category: str) -> List[TestData]:
        """
        Find records by category.
        """
        return [
            record
            for record in self._repository.values()
            if record.category == category
        ]

    def find_by_tag(self, tag: str) -> List[TestData]:
        """
        Find records containing a tag.
        """
        return [
            record
            for record in self._repository.values()
            if tag in record.tags
        ]

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save_to_json(self, file_path: str | Path) -> None:
        """
        Save repository to a JSON file.
        """
        path = Path(file_path)

        with path.open("w", encoding="utf-8") as file:
            json.dump(
                [record.to_dict() for record in self.get_all()],
                file,
                indent=4,
                default=str,
            )

        logger.info("Repository saved to %s", path)

    def load_from_json(self, file_path: str | Path) -> None:
        """
        Load repository from a JSON file.
        """
        path = Path(file_path)

        if not path.exists():
            logger.warning("Repository file not found: %s", path)
            return

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        self.clear()

        for item in data:
            self.add(TestData.from_dict(item))

        logger.info("Repository loaded from %s", path)

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def statistics(self) -> Dict[str, int]:
        """
        Return repository statistics.
        """
        return {
            "total_records": self.count()
        }
