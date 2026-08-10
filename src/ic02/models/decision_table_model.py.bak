"""
Decision Table Model

Represents one decision table rule generated from a requirement.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class DecisionTableModel:
    """
    Represents one decision table rule.
    """

    requirement_id: str
    rule_id: str
    conditions: List[str]
    actions: List[str]
    expected_result: str
