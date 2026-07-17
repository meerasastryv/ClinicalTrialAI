"""
IC-07 Data Set Repository

Provides repository operations for DataSet objects.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional

from src.ic07.models.data_set import DataSet

logger = logging.getLogger(__name__)


class DataSetRepository:
    """
    Repository for managing DataSet objects.
    """

    def __init__(self) -> None:
        self._repository: Dict[str, DataSet] = {}

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def add(self, dataset: DataSet) -> None:
        """Add or update a DataSet."""
        self._repository[dataset.dataset_id] = dataset
        logger.info("Stored DataSet: %s", dataset.dataset_id)

    def get(self, dataset_id: str) -> Optional[DataSet]:
        """Retrieve a DataSet by ID."""
        return self._repository.get(dataset_id)

    def update(self, dataset: DataSet) -> None:
        """Update an existing DataSet."""
        self._repository[dataset.dataset_id] = dataset
        logger.info("Updated DataSet: %s", dataset.dataset_id)

    def delete(self, dataset_id: str) -> bool:
        """Delete a DataSet."""
        if dataset_id in self._repository:
            del self._repository[dataset_id]
            logger.info("Deleted DataSet: %s", dataset_id)
            return True
        return False

    # ------------------------------------------------------------------
    # Retrieval
    # ------------------------------------------------------------------

    def get_all(self) -> List[DataSet]:
        """Return all datasets."""
        return list(self._repository.values())

    def exists(self, dataset_id: str) -> bool:
        """Check whether a dataset exists."""
        return dataset_id in self._repository

    def count(self) -> int:
        """Return the number of datasets."""
        return len(self._repository)

    def clear(self) -> None:
        """Remove all datasets."""
        self._repository.clear()
        logger.info("Repository cleared.")

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_name(self, name: str) -> List[DataSet]:
        """Find datasets by name."""
        return [
            dataset
            for dataset in self._repository.values()
            if dataset.name.lower() == name.lower()
        ]

    def find_by_tag(self, tag: str) -> List[DataSet]:
        """Find datasets containing a tag."""
        return [
            dataset
            for dataset in self._repository.values()
            if tag in dataset.tags
        ]

    def find_by_source(self, source: str) -> List[DataSet]:
        """Find datasets by source."""
        return [
            dataset
            for dataset in self._repository.values()
            if dataset.source.lower() == source.lower()
        ]

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save_to_json(self, file_path: str | Path) -> None:
        """Save repository to a JSON file."""
        path = Path(file_path)

        with path.open("w", encoding="utf-8") as file:
            json.dump(
                [dataset.to_dict() for dataset in self.get_all()],
                file,
                indent=4,
            )

        logger.info("Repository saved to %s", path)

    def load_from_json(self, file_path: str | Path) -> None:
        """Load repository from a JSON file."""
        path = Path(file_path)

        if not path.exists():
            logger.warning("Repository file not found: %s", path)
            return

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        self.clear()

        for item in data:
            self.add(DataSet.from_dict(item))

        logger.info("Repository loaded from %s", path)

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def statistics(self) -> Dict[str, int]:
        """Return repository statistics."""

        total_records = sum(
            dataset.record_count
            for dataset in self._repository.values()
        )

        total_fields = sum(
            dataset.field_count
            for dataset in self._repository.values()
        )

        return {
            "total_datasets": self.count(),
            "total_records": total_records,
            "total_fields": total_fields,
        }
