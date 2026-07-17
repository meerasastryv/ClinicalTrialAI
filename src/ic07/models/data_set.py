"""
IC-07 Data Set Model

Represents a collection of test data records.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict, List

from src.ic07.models.data_field import DataField
from src.ic07.models.test_data import TestData


@dataclass
class DataSet:
    """
    Represents a logical collection of test data.
    """

    # ------------------------------------------------------------------
    # Identification
    # ------------------------------------------------------------------

    dataset_id: str

    name: str

    description: str = ""

    source: str = ""

    version: str = "1.0"

    # ------------------------------------------------------------------
    # Dataset Contents
    # ------------------------------------------------------------------

    fields: List[DataField] = field(default_factory=list)

    records: List[TestData] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    tags: List[str] = field(default_factory=list)

    created_by: str = "System"

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime | None = None

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_field(self, data_field: DataField) -> None:
        """Add a field definition."""
        self.fields.append(data_field)

    def add_record(self, record: TestData) -> None:
        """Add a test data record."""
        self.records.append(record)

    def add_tag(self, tag: str) -> None:
        """Add a dataset tag."""
        if tag not in self.tags:
            self.tags.append(tag)

    @property
    def field_count(self) -> int:
        """Return the number of fields."""
        return len(self.fields)

    @property
    def record_count(self) -> int:
        """Return the number of records."""
        return len(self.records)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataset to a dictionary."""

        return {
            "dataset_id": self.dataset_id,
            "name": self.name,
            "description": self.description,
            "source": self.source,
            "version": self.version,
            "fields": [field.to_dict() for field in self.fields],
            "records": [record.to_dict() for record in self.records],
            "tags": self.tags,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat(),
            "updated_at": (
                self.updated_at.isoformat()
                if self.updated_at
                else None
            ),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataSet":
        """Create a DataSet from a dictionary."""

        return cls(
            dataset_id=data["dataset_id"],
            name=data["name"],
            description=data.get("description", ""),
            source=data.get("source", ""),
            version=data.get("version", "1.0"),
            fields=[
                DataField.from_dict(field)
                for field in data.get("fields", [])
            ],
            records=[
                TestData.from_dict(record)
                for record in data.get("records", [])
            ],
            tags=data.get("tags", []),
            created_by=data.get("created_by", "System"),
            created_at=datetime.fromisoformat(data["created_at"])
            if data.get("created_at")
            else datetime.utcnow(),
            updated_at=datetime.fromisoformat(data["updated_at"])
            if data.get("updated_at")
            else None,
        )
