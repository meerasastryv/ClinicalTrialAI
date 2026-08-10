"""
IC-08 - Platform Usage Intelligence
Milestone 16 - Study Health Repository
"""

from typing import Dict, List, Optional

from src.ic08.models.study_health import StudyHealth


class StudyHealthRepository:
    """
    Repository for storing and retrieving Study Health Index results.
    """

    def __init__(self):
        self._studies: Dict[str, StudyHealth] = {}

    def save(self, study_health: StudyHealth) -> None:
        """
        Save or update a study's health record.
        """
        self._studies[study_health.study_id] = study_health

    def find_by_study(
        self,
        study_id: str
    ) -> Optional[StudyHealth]:
        """
        Retrieve Study Health by study ID.
        """
        return self._studies.get(study_id)

    def find_all(self) -> List[StudyHealth]:
        """
        Return all Study Health records.
        """
        return list(self._studies.values())

    def average_health(self) -> float:
        """
        Calculate the average Study Health Index.
        """
        if not self._studies:
            return 0.0

        total = sum(
            study.health_score
            for study in self._studies.values()
        )

        return total / len(self._studies)

    def top_healthy_studies(
        self,
        limit: int = 5
    ) -> List[StudyHealth]:
        """
        Return the healthiest studies.
        """
        return sorted(
            self._studies.values(),
            key=lambda study: study.health_score,
            reverse=True
        )[:limit]

    def count(self) -> int:
        """
        Return the number of stored studies.
        """
        return len(self._studies)

    def clear(self) -> None:
        """
        Remove all stored Study Health records.
        """
        self._studies.clear()

    def exists(self, study_id: str) -> bool:
        """
        Check whether a study exists.
        """
        return study_id in self._studies

    def remove(self, study_id: str) -> bool:
        """
        Remove a Study Health record.

        Returns True if removed successfully.
        """
        if study_id in self._studies:
            del self._studies[study_id]
            return True

        return False
