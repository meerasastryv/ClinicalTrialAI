"""
Repository for intelligent data cleansing actions.
"""

from __future__ import annotations

from typing import List

from src.ic07.models.cleansing_action import (
    CleansingAction,
)


class CleansingRepository:
    """
    Repository for storing cleansing actions.
    """

    def __init__(self) -> None:
        self._actions: List[
            CleansingAction
        ] = []

    # ------------------------------------------------------------------

    def add(
        self,
        action: CleansingAction,
    ) -> None:
        """
        Add a cleansing action.
        """
        self._actions.append(action)

    # ------------------------------------------------------------------

    def list_all(
        self,
    ) -> List[CleansingAction]:
        """
        Return all cleansing actions.
        """
        return self._actions

    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Remove all cleansing actions.
        """
        self._actions.clear()

    # ------------------------------------------------------------------

    def count(self) -> int:
        """
        Return number of cleansing actions.
        """
        return len(self._actions)

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return self.count()

    def __iter__(self):
        return iter(self._actions)
