from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class CustomerIntelligence:
    """
    Consolidated intelligence dashboard for a customer/study.

    NOTE:
    This model will be renamed to StudyIntelligence during the
    IC-08 production refactoring milestone.
    """

    # Customer / Study Information
    customer_id: str
    organization_name: str
    study_id: Optional[str] = None
    study_name: Optional[str] = None

    # Intelligence Scores
    health_score: float = 0.0
    engagement_score: float = 0.0
    adoption_score: float = 0.0
    workflow_score: float = 0.0
    journey_score: float = 0.0
    study_health_score: float = 0.0

    # Overall Metrics
    overall_score: float = 0.0
    risk_level: str = "UNKNOWN"

    # Usage Statistics
    total_users: int = 0
    active_sessions: int = 0
    average_session_duration: float = 0.0

    # Workflow Metrics
    workflow_completion: float = 0.0

    # Journey Metrics
    journey_completion: float = 0.0
    drop_off_rate: float = 0.0

    # Feature Analytics
    top_features: List[str] = field(default_factory=list)
    least_used_features: List[str] = field(default_factory=list)

    # Trend Analytics
    trend_summary: Dict[str, float] = field(default_factory=dict)

    # AI Recommendations
    recommendations: List[str] = field(default_factory=list)

    # Executive Summary
    executive_summary: str = ""

    def to_dict(self) -> Dict:
        """
        Convert the dashboard into a dictionary.
        """
        return {
            "customer_id": self.customer_id,
            "organization_name": self.organization_name,
            "study_id": self.study_id,
            "study_name": self.study_name,
            "health_score": self.health_score,
            "engagement_score": self.engagement_score,
            "adoption_score": self.adoption_score,
            "workflow_score": self.workflow_score,
            "journey_score": self.journey_score,
            "study_health_score": self.study_health_score,
            "overall_score": self.overall_score,
            "risk_level": self.risk_level,
            "total_users": self.total_users,
            "active_sessions": self.active_sessions,
            "average_session_duration": self.average_session_duration,
            "workflow_completion": self.workflow_completion,
            "journey_completion": self.journey_completion,
            "drop_off_rate": self.drop_off_rate,
            "top_features": self.top_features,
            "least_used_features": self.least_used_features,
            "trend_summary": self.trend_summary,
            "recommendations": self.recommendations,
            "executive_summary": self.executive_summary,
        }

    def __str__(self) -> str:
        return (
            f"CustomerIntelligence("
            f"customer='{self.organization_name}', "
            f"study='{self.study_name}', "
            f"overall_score={self.overall_score:.2f}, "
            f"risk='{self.risk_level}')"
        )
