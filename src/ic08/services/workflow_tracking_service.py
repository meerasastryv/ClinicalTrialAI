"""
workflow_tracking_service.py

Service responsible for tracking customer workflows.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from src.ic08.models.workflow import Workflow
from src.ic08.repositories.workflow_repository import WorkflowRepository


class WorkflowTrackingService:
    """
    Service for managing workflow execution statistics.
    """

    def __init__(
        self,
        workflow_repository: WorkflowRepository,
    ) -> None:
        self._repository = workflow_repository

    def register_workflow(
        self,
        workflow: Workflow,
    ) -> None:
        """
        Registers a workflow.
        """
        self._repository.add_workflow(workflow)

    def record_workflow_execution(
        self,
        workflow_id: str,
        duration_ms: int,
        completed: bool,
    ) -> bool:
        """
        Records a workflow execution.

        Returns
        -------
        bool
            True if the workflow exists and was updated.
        """
        workflow = self._repository.get_workflow(workflow_id)

        if workflow is None:
            return False

        workflow.increment_execution()

        total_duration = (
            workflow.average_duration_ms
            * (workflow.execution_count - 1)
        ) + duration_ms

        workflow.average_duration_ms = (
            total_duration / workflow.execution_count
        )

        if completed:
            completed_runs = (
                workflow.completion_rate
                * (workflow.execution_count - 1)
                / 100
            ) + 1
        else:
            completed_runs = (
                workflow.completion_rate
                * (workflow.execution_count - 1)
                / 100
            )

        workflow.completion_rate = (
            completed_runs / workflow.execution_count
        ) * 100

        workflow.updated_at = datetime.utcnow()

        self._repository.update_workflow(workflow)

        return True

    def get_workflow(
        self,
        workflow_id: str,
    ) -> Optional[Workflow]:
        """
        Returns a workflow by ID.
        """
        return self._repository.get_workflow(workflow_id)

    def get_most_executed_workflow(
        self,
    ) -> Optional[Workflow]:
        """
        Returns the most frequently executed workflow.
        """
        return self._repository.get_most_executed_workflow()

    def get_longest_workflow(
        self,
    ) -> Optional[Workflow]:
        """
        Returns the workflow with the highest average duration.
        """
        return self._repository.get_longest_workflow()

    def total_workflows(self) -> int:
        """
        Returns the total number of workflows.
        """
        return self._repository.total_workflows()
