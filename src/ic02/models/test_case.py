#from dataclasses import dataclass
#from typing import List


#@dataclass
#class TestCase:
#    testcase_id: str
#    scenario_id: str
#    title: str
#    preconditions: List[str]
#    steps: List[str]
#    expected_results: List[str]

from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:

    testcase_id: str

    requirement_id: str

    scenario_id: str

    condition_id: str

    title: str

    priority: str

    test_type: str

    automation_candidate: bool

    preconditions: List[str]

    steps: List[str]

    expected_results: List[str]
