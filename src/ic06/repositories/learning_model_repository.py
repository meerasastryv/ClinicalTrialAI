"""
learning_model_repository.py

Adaptive Learning Engine

Repository for LearningModel objects.

Provides:

- Storage
- CRUD operations
- Search
- Statistics
- Import/Export
- Filtering

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

import json

from pathlib import Path
from typing import Dict, List, Optional

from src.ic06.models.learning_model import LearningModel


class LearningModelRepository:
    """
    Repository for LearningModel objects.
    """

    def __init__(self) -> None:

        self._models: Dict[str, LearningModel] = {}

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(
        self,
        model: LearningModel,
    ) -> None:
        """
        Adds a learning model.
        """
        self._models[model.model_id] = model

    def update(
        self,
        model: LearningModel,
    ) -> None:
        """
        Updates an existing learning model.
        """
        self._models[model.model_id] = model

    def remove(
        self,
        model_id: str,
    ) -> bool:
        """
        Removes a learning model.

        Returns
        -------
        bool
            True if removed.
        """
        return (
            self._models.pop(model_id, None)
            is not None
        )

    def get(
        self,
        model_id: str,
    ) -> Optional[LearningModel]:
        """
        Returns a learning model.
        """
        return self._models.get(model_id)

    def exists(
        self,
        model_id: str,
    ) -> bool:
        """
        Returns True if the learning model exists.
        """
        return model_id in self._models

    def clear(self) -> None:
        """
        Removes all learning models.
        """
        self._models.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    def get_all(self) -> List[LearningModel]:
        """
        Returns all learning models.
        """
        return list(self._models.values())

    def count(self) -> int:
        """
        Returns repository size.
        """
        return len(self._models)


    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_version(
        self,
        version: str,
    ) -> List[LearningModel]:
        """
        Returns all learning models matching the specified version.
        """
        return [
            model
            for model in self._models.values()
            if model.version == version
        ]

    def find_by_confidence(
        self,
        minimum_confidence: float,
    ) -> List[LearningModel]:
        """
        Returns all learning models with overall confidence greater
        than or equal to the specified threshold.
        """
        return [
            model
            for model in self._models.values()
            if model.overall_confidence >= minimum_confidence
        ]

    def find_latest(self) -> Optional[LearningModel]:
        """
        Returns the most recently updated learning model.
        """
        if not self._models:
            return None

        return max(
            self._models.values(),
            key=lambda model: model.last_updated,
        )

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def sort_by_created_at(
        self,
        reverse: bool = True,
    ) -> List[LearningModel]:
        """
        Returns learning models sorted by creation time.
        """
        return sorted(
            self._models.values(),
            key=lambda model: model.created_at,
            reverse=reverse,
        )

    def sort_by_last_updated(
        self,
        reverse: bool = True,
    ) -> List[LearningModel]:
        """
        Returns learning models sorted by last update time.
        """
        return sorted(
            self._models.values(),
            key=lambda model: model.last_updated,
            reverse=reverse,
        )

    def sort_by_confidence(
        self,
        reverse: bool = True,
    ) -> List[LearningModel]:
        """
        Returns learning models sorted by overall confidence.
        """
        return sorted(
            self._models.values(),
            key=lambda model: model.overall_confidence,
            reverse=reverse,
        )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def average_confidence(self) -> float:
        """
        Returns the average overall confidence.
        """
        if not self._models:
            return 0.0

        total = sum(
            model.overall_confidence
            for model in self._models.values()
        )

        return total / len(self._models)

    def version_counts(self) -> Dict[str, int]:
        """
        Returns the number of learning models by version.
        """
        counts: Dict[str, int] = {}

        for model in self._models.values():
            version = model.version
            counts[version] = (
                counts.get(version, 0) + 1
            )

        return counts

    def total_learning_events(self) -> int:
        """
        Returns the total number of learning events across all models.
        """
        return sum(
            model.event_count()
            for model in self._models.values()
        )

    def total_learning_patterns(self) -> int:
        """
        Returns the total number of learning patterns across all models.
        """
        return sum(
            model.pattern_count()
            for model in self._models.values()
        )

    def total_feedback_records(self) -> int:
        """
        Returns the total number of feedback records across all models.
        """
        return sum(
            model.feedback_count()
            for model in self._models.values()
        )

    def total_snapshots(self) -> int:
        """
        Returns the total number of knowledge snapshots across all models.
        """
        return sum(
            model.snapshot_count()
            for model in self._models.values()
        )

    # ------------------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------------------

    def export_to_json(
        self,
        file_path: str,
    ) -> None:
        """
        Exports all learning models to a JSON file.

        Args:
            file_path:
                Destination JSON file.
        """
        data = [
            model.to_dict()
            for model in self.get_all()
        ]

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def import_from_json(
        self,
        file_path: str,
    ) -> None:
        """
        Imports learning models from a JSON file.

        Args:
            file_path:
                Source JSON file.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        self.clear()

        for item in data:
            model = LearningModel.from_dict(item)
            self.add(model)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict[str, object]:
        """
        Returns repository summary statistics.
        """
        latest = self.find_latest()

        return {
            "total_models": self.count(),
            "latest_model":
                latest.name if latest else None,
            "average_confidence":
                self.average_confidence(),
            "version_counts":
                self.version_counts(),
            "total_learning_events":
                self.total_learning_events(),
            "total_learning_patterns":
                self.total_learning_patterns(),
            "total_feedback_records":
                self.total_feedback_records(),
            "total_snapshots":
                self.total_snapshots(),
        }

    # ------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns the number of stored learning models.
        """
        return self.count()

    def __iter__(self):
        """
        Iterates over stored learning models.
        """
        return iter(
            self._models.values()
        )

    def __contains__(
        self,
        model_id: str,
    ) -> bool:
        """
        Returns True if the repository contains the learning model.
        """
        return self.exists(model_id)

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"LearningModelRepository("
            f"models={self.count()}, "
            f"average_confidence="
            f"{self.average_confidence():.2f}, "
            f"events={self.total_learning_events()}, "
            f"patterns={self.total_learning_patterns()})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()
