"""
workflow.py

Workflow model for the Customer Usage Intelligence Engine.

Represents a business workflow executed by customers. A workflow is a
sequence of related usage events that together accomplish a business task.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Workflow:
    """
    Represents a customer workflow.
    """

    workflow_id: str
    workflow_name: str
    description: str

    steps: list[str] = field(default_factory=list)

    execution_count: int = 0

    average_duration_ms: float = 0.0

    completion_rate: float = 0.0

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def add_step(self, step: str) -> None:
        """
        Adds a step to the workflow.
        """
        self.steps.append(step)
        self.updated_at = datetime.utcnow()

    def increment_execution(self) -> None:
        """
        Increments the workflow execution count.
        """
        self.execution_count += 1
        self.updated_at = datetime.utcnow()

    def update_completion_rate(
        self,
        completed: int,
        total: int,
    ) -> None:
        """
        Updates the workflow completion percentage.
        """
        if total == 0:
            self.completion_rate = 0.0
        else:
            self.completion_rate = (completed / total) * 100

        self.updated_at = datetime.utcnow()
