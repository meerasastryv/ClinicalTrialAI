from typing import Dict, List

from src.ic04.models.runtime_relationship import RuntimeRelationship


class RuntimeGraphRepository:
    """
    Stores runtime caller-callee relationships.
    """

    def __init__(self):

        self._relationships: Dict[str, RuntimeRelationship] = {}

    def add_relationship(
        self,
        caller: str,
        callee: str,
        duration_ms: float = 0.0,
    ):

        key = f"{caller}->{callee}"

        if key not in self._relationships:

            self._relationships[key] = RuntimeRelationship(
                caller=caller,
                callee=callee,
                call_count=0,
                total_duration_ms=0.0,
            )

        relationship = self._relationships[key]

        relationship.call_count += 1
        relationship.total_duration_ms += duration_ms

    def get_relationships(self) -> List[RuntimeRelationship]:

        return list(self._relationships.values())

    def size(self):

        return len(self._relationships)
