"""
base_repository.py

Platform Foundation (PF-01)

Generic repository implementation used throughout the ClinicalTrialAI
platform.

Provides reusable CRUD, collection management and query operations
for all domain repositories.

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, Iterator, List, Optional, TypeVar


T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """
    Generic base repository.

    Provides common CRUD and collection management operations.
    """

    def __init__(self) -> None:
        self._items: Dict[str, T] = {}

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _get_item_id(self, item: T) -> str:
        """
        Returns the unique identifier for the item.

        Derived repositories must override this method.
        """
        raise NotImplementedError(
            "_get_item_id() must be implemented."
        )

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(self, item: T) -> None:
        """
        Adds an item to the repository.
        """
        self._items[self._get_item_id(item)] = item

    def update(self, item: T) -> None:
        """
        Updates an existing item.
        """
        self._items[self._get_item_id(item)] = item

    def remove(self, item_id: str) -> bool:
        """
        Removes an item by ID.

        Returns:
            True if the item existed and was removed.
        """
        return self._items.pop(item_id, None) is not None

    def get(self, item_id: str) -> Optional[T]:
        """
        Returns an item by ID.
        """
        return self._items.get(item_id)

    def exists(self, item_id: str) -> bool:
        """
        Returns True if the item exists.
        """
        return item_id in self._items

    def clear(self) -> None:
        """
        Removes all items.
        """
        self._items.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    def get_all(self) -> List[T]:
        """
        Returns all items.
        """
        return list(self._items.values())

    def count(self) -> int:
        """
        Returns the number of stored items.
        """
        return len(self._items)

    def is_empty(self) -> bool:
        """
        Returns True if the repository is empty.
        """
        return len(self._items) == 0

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict[str, int]:
        """
        Returns repository summary information.

        Returns:
            Dictionary containing repository statistics.
        """
        return {
            "count": self.count(),
            "is_empty": self.is_empty(),
        }

    # ------------------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------------------

    def export_to_dict(self) -> List[dict]:
        """
        Exports all repository items to a list of dictionaries.

        Returns:
            List of serialized items.
        """
        exported: List[dict] = []

        for item in self.get_all():
            if hasattr(item, "to_dict"):
                exported.append(item.to_dict())

        return exported

    def import_from_dict(
        self,
        items: List[T],
    ) -> None:
        """
        Imports items into the repository.

        Existing items are cleared.

        Args:
            items:
                Items to import.
        """
        self.clear()

        for item in items:
            self.add(item)

    # ------------------------------------------------------------------
    # Iteration
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns repository size.
        """
        return self.count()

    def __iter__(self) -> Iterator[T]:
        """
        Iterates over repository items.
        """
        return iter(self._items.values())

    def __contains__(
        self,
        item_id: str,
    ) -> bool:
        """
        Returns True if the repository contains the specified ID.
        """
        return self.exists(item_id)

    # ------------------------------------------------------------------
    # String Representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"{self.__class__.__name__}"
            f"(count={self.count()})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


