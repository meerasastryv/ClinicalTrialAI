"""
database_query_collector.py

Collects runtime database query information.
"""

from src.ic04.models.database_query import DatabaseQuery
from src.ic04.repositories.database_query_repository import (
    DatabaseQueryRepository,
)


class DatabaseQueryCollector:
    """
    Collects database queries during runtime.
    """

    def __init__(self):
        self.repository = DatabaseQueryRepository()

    def collect(
        self,
        operation: str,
        table_name: str,
        caller_method: str,
        duration_ms: float,
        rows_affected: int = 0,
    ):
        """
        Record a database query.
        """

        query = DatabaseQuery(
            operation=operation,
            table_name=table_name,
            caller_method=caller_method,
            duration_ms=duration_ms,
            rows_affected=rows_affected,
        )

        self.repository.add_query(query)

    def get_repository(self):
        """
        Return the repository.
        """
        return self.repository

    def get_total_queries(self):
        """
        Return total number of queries.
        """
        return self.repository.get_total_queries()

    def clear(self):
        """
        Remove all collected queries.
        """
        self.repository.clear()
