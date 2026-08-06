"""
Change Request Model

Represents a requested change that will be analyzed for impact.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class ChangeRequest:
    """
    Represents a change submitted for impact analysis.
    """

    change_id: str

    artifact_id: str

    artifact_type: str

    title: str

    description: str = ""

    requested_by: str = ""

    priority: str = "MEDIUM"

    status: str = "NEW"

    created_at: datetime = field(default_factory=datetime.utcnow)

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert object to dictionary.
        """
        return {
            "change_id": self.change_id,
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "title": self.title,
            "description": self.description,
            "requested_by": self.requested_by,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ChangeRequest":
        """
        Build object from dictionary.
        """
        created_at = data.get("created_at")

        return cls(
            change_id=data.get("change_id", ""),
            artifact_id=data.get("artifact_id", ""),
            artifact_type=data.get("artifact_type", ""),
            title=data.get("title", ""),
            description=data.get("description", ""),
            requested_by=data.get("requested_by", ""),
            priority=data.get("priority", "MEDIUM"),
            status=data.get("status", "NEW"),
            created_at=datetime.fromisoformat(created_at)
            if created_at
            else datetime.utcnow(),
            metadata=data.get("metadata", {}),
        )
