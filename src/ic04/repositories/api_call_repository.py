"""
api_call_repository.py

Repository for storing runtime API calls.
"""

from typing import List

from src.ic04.models.api_call import ApiCall


class ApiCallRepository:
    """
    Repository for runtime API calls.
    """

    def __init__(self):
        self._api_calls: List[ApiCall] = []

    def add_api_call(self, api_call: ApiCall):
        """
        Store an API call.
        """
        self._api_calls.append(api_call)

    def get_all_api_calls(self) -> List[ApiCall]:
        """
        Return all API calls.
        """
        return list(self._api_calls)

    def get_api_calls_by_method(
        self,
        http_method: str
    ) -> List[ApiCall]:
        """
        Return API calls matching an HTTP method.
        """
        return [
            api_call
            for api_call in self._api_calls
            if api_call.http_method == http_method
        ]

    def get_api_calls_by_status(
        self,
        status_code: int
    ) -> List[ApiCall]:
        """
        Return API calls matching a status code.
        """
        return [
            api_call
            for api_call in self._api_calls
            if api_call.status_code == status_code
        ]

    def get_total_calls(self) -> int:
        """
        Return the total number of API calls.
        """
        return len(self._api_calls)

    def get_average_duration(self) -> float:
        """
        Return the average API response time.
        """

        if not self._api_calls:
            return 0.0

        return (
            sum(call.duration_ms for call in self._api_calls)
            / len(self._api_calls)
        )

    def clear(self):
        """
        Remove all API calls.
        """
        self._api_calls.clear()

    def __len__(self):
        return len(self._api_calls)

    def __iter__(self):
        return iter(self._api_calls)

    def __str__(self):
        return (
            f"ApiCallRepository("
            f"calls={len(self._api_calls)})"
        )
