"""
api_call_collector.py

Collects runtime API call information.
"""

from src.ic04.models.api_call import ApiCall
from src.ic04.repositories.api_call_repository import ApiCallRepository


class ApiCallCollector:
    """
    Collects API calls during runtime.
    """

    def __init__(self):
        self.repository = ApiCallRepository()

    def collect(
        self,
        endpoint: str,
        http_method: str,
        caller_method: str,
        duration_ms: float,
        status_code: int = 200,
    ):
        """
        Record an API call.
        """

        api_call = ApiCall(
            endpoint=endpoint,
            http_method=http_method,
            caller_method=caller_method,
            duration_ms=duration_ms,
            status_code=status_code,
        )

        self.repository.add_api_call(api_call)

    def get_repository(self):
        """
        Return the repository.
        """
        return self.repository

    def get_total_calls(self):
        """
        Total API calls.
        """
        return self.repository.get_total_calls()

    def clear(self):
        """
        Clear collected API calls.
        """
        self.repository.clear()
