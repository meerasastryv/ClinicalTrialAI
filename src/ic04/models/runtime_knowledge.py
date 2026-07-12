from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class RuntimeKnowledge:
    """
    Consolidated Runtime Knowledge.

    This object represents the complete runtime knowledge
    produced by the Runtime Exploration Agent.
    """

    runtime_repository: Any = None
    performance_repository: Any = None
    hotspot_repository: Any = None
    api_call_repository: Any = None
    database_query_repository: Any = None

    execution_summary: Dict[str, int] = field(default_factory=dict)

    def total_artifacts(self) -> int:
        """
        Returns the total number of runtime artifacts captured.
        """

        total = 0

        if self.runtime_repository is not None:
            total += self.runtime_repository.size()

        if self.performance_repository is not None:
            total += len(
                self.performance_repository.get_all_metrics()
            )

        if self.hotspot_repository is not None:
            total += len(
                self.hotspot_repository.get_all_hotspots()
            )

        if self.api_call_repository is not None:
            total += len(
                self.api_call_repository.get_all_api_calls()
            )

        if self.database_query_repository is not None:
            total += len(
                self.database_query_repository.get_all_queries()
            )

        return total
