from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    testcase_id: str
    scenario_id: str
    title: str
    preconditions: List[str]
    steps: List[str]
    expected_results: List[str]
