from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class FeatureAdoption:
    """
    Represents adoption analytics for a product feature.
    """

    feature_name: str

    total_users: int = 0
    adopted_users: int = 0

    adoption_rate: float = 0.0
    repeat_usage_rate: float = 0.0

    total_usage_count: int = 0
    average_usage: float = 0.0

    first_use: Optional[datetime] = None
    last_use: Optional[datetime] = None

    time_to_adoption: float = 0.0

    power_users: int = 0
    casual_users: int = 0
    inactive_users: int = 0

    trend: str = "Stable"

    score: float = 0.0

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "feature_name": self.feature_name,
            "total_users": self.total_users,
            "adopted_users": self.adopted_users,
            "adoption_rate": self.adoption_rate,
            "repeat_usage_rate": self.repeat_usage_rate,
            "total_usage_count": self.total_usage_count,
            "average_usage": self.average_usage,
            "first_use": self.first_use.isoformat() if self.first_use else None,
            "last_use": self.last_use.isoformat() if self.last_use else None,
            "time_to_adoption": self.time_to_adoption,
            "power_users": self.power_users,
            "casual_users": self.casual_users,
            "inactive_users": self.inactive_users,
            "trend": self.trend,
            "score": self.score,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FeatureAdoption":
        return cls(
            feature_name=data.get("feature_name", ""),
            total_users=data.get("total_users", 0),
            adopted_users=data.get("adopted_users", 0),
            adoption_rate=data.get("adoption_rate", 0.0),
            repeat_usage_rate=data.get("repeat_usage_rate", 0.0),
            total_usage_count=data.get("total_usage_count", 0),
            average_usage=data.get("average_usage", 0.0),
            first_use=datetime.fromisoformat(data["first_use"])
            if data.get("first_use")
            else None,
            last_use=datetime.fromisoformat(data["last_use"])
            if data.get("last_use")
            else None,
            time_to_adoption=data.get("time_to_adoption", 0.0),
            power_users=data.get("power_users", 0),
            casual_users=data.get("casual_users", 0),
            inactive_users=data.get("inactive_users", 0),
            trend=data.get("trend", "Stable"),
            score=data.get("score", 0.0),
            created_at=datetime.fromisoformat(data["created_at"])
            if data.get("created_at")
            else datetime.utcnow(),
            updated_at=datetime.fromisoformat(data["updated_at"])
            if data.get("updated_at")
            else datetime.utcnow(),
        )

    def update_timestamp(self) -> None:
        self.updated_at = datetime.utcnow()

    def __str__(self) -> str:
        return (
            f"FeatureAdoption("
            f"feature='{self.feature_name}', "
            f"adoption_rate={self.adoption_rate:.2f}%, "
            f"adopted_users={self.adopted_users}/{self.total_users}, "
            f"average_usage={self.average_usage:.2f}, "
            f"score={self.score:.2f}, "
            f"trend='{self.trend}')"
        )

     
