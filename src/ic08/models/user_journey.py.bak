"""
user_journey.py

User journey model for the Customer Usage Intelligence Engine.

Represents an end-to-end customer journey through the application.
A journey consists of multiple workflow steps and provides insight
into user behavior, completion rates, and drop-off points.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class UserJourney:
    """
    Represents a customer journey.
    """

    journey_id: str
    journey_name: str
    description: str

    steps: list[str] = field(default_factory=list)

    start_event: str = ""
    end_event: str = ""

    completion_rate: float = 0.0

    drop_off_points: list[str] = field(default_factory=list)

    average_duration_ms: float = 0.0

    total_executions: int = 0

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def add_step(self, step: str) -> None:
        """
        Adds a step to the customer journey.
        """
        self.steps.append(step)
        self.updated_at = datetime.utcnow()

    def add_drop_off_point(self, step: str) -> None:
        """
        Records a drop-off point within the journey.
        """
        if step not in self.drop_off_points:
            self.drop_off_points.append(step)
            self.updated_at = datetime.utcnow()

    def increment_execution(self) -> None:
        """
        Increments the execution count.
        """
        self.total_executions += 1
        self.updated_at = datetime.utcnow()

    def update_completion_rate(
        self,
        completed: int,
        total: int,
    ) -> None:
        """
        Updates the completion percentage.
        """
        if total == 0:
            self.completion_rate = 0.0
        else:
            self.completion_rate = (completed / total) * 100

        self.updated_at = datetime.utcnow()
