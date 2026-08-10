"""
workflow_repository.py

Repository for managing Workflow objects.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.ic08.models.workflow import Workflow


class WorkflowRepository:
    """
    Repository for storing and analyzing customer workflows.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._workflows: Dict[str, Workflow] = {}

    def add_workflow(
        self,
        workflow: Workflow,
    ) -> None:
        """
        Adds or replaces a workflow.
        """
        self._workflows[workflow.workflow_id] = workflow

    def get_workflow(
        self,
        workflow_id: str,
    ) -> Optional[Workflow]:
        """
        Returns a workflow by ID.
        """
        return self._workflows.get(workflow_id)

    def update_workflow(
        self,
        workflow: Workflow,
    ) -> None:
        """
        Updates an existing workflow.
        """
        self._workflows[workflow.workflow_id] = workflow

    def remove_workflow(
        self,
        workflow_id: str,
    ) -> bool:
        """
        Removes a workflow.
        """
        return self._workflows.pop(workflow_id, None) is not None

    def get_all_workflows(self) -> List[Workflow]:
        """
        Returns all workflows.
        """
        return list(self._workflows.values())

    def get_most_executed_workflow(self) -> Optional[Workflow]:
        """
        Returns the most frequently executed workflow.
        """
        if not self._workflows:
            return None

        return max(
            self._workflows.values(),
            key=lambda workflow: workflow.execution_count,
        )

    def get_longest_workflow(self) -> Optional[Workflow]:
        """
        Returns the workflow with the highest average duration.
        """
        if not self._workflows:
            return None

        return max(
            self._workflows.values(),
            key=lambda workflow: workflow.average_duration_ms,
        )

    def get_high_completion_workflows(
        self,
        threshold: float = 95.0,
    ) -> List[Workflow]:
        """
        Returns workflows with completion rates above the threshold.
        """
        return [
            workflow
            for workflow in self._workflows.values()
            if workflow.completion_rate >= threshold
        ]

    def get_workflows_with_multiple_steps(
        self,
        minimum_steps: int = 5,
    ) -> List[Workflow]:
        """
        Returns workflows containing at least the specified number of steps.
        """
        return [
            workflow
            for workflow in self._workflows.values()
            if len(workflow.steps) >= minimum_steps
        ]

    def workflow_exists(
        self,
        workflow_id: str,
    ) -> bool:
        """
        Checks whether a workflow exists.
        """
        return workflow_id in self._workflows

    def total_workflows(self) -> int:
        """
        Returns the total number of workflows.
        """
        return len(self._workflows)

    def clear(self) -> None:
        """
        Removes all workflows.
        """
        self._workflows.clear()
