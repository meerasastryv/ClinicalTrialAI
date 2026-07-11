"""
database_query_repository.py

Repository for storing runtime database queries.
"""

from typing import List

from src.ic04.models.database_query import DatabaseQuery


class DatabaseQueryRepository:
    """
    Repository for runtime database queries.
    """

    def __init__(self):
        self._queries: List[DatabaseQuery] = []

    def add_query(self, query: DatabaseQuery):
        """
        Store a database query.
        """
        self._queries.append(query)

    def get_all_queries(self) -> List[DatabaseQuery]:
        """
        Return all captured database queries.
        """
        return list(self._queries)

    def get_queries_by_operation(
        self,
        operation: str
    ) -> List[DatabaseQuery]:
        """
        Return queries matching an operation.
        """
        return [
            query
            for query in self._queries
            if query.operation == operation
        ]

    def get_queries_by_table(
        self,
        table_name: str
    ) -> List[DatabaseQuery]:
        """
        Return queries executed on a table.
        """
        return [
            query
            for query in self._queries
            if query.table_name == table_name
        ]

    def get_total_queries(self) -> int:
        """
        Total number of queries.
        """
        return len(self._queries)

    def get_average_duration(self) -> float:
        """
        Average query execution time.
        """

        if not self._queries:
            return 0.0

        return (
            sum(query.duration_ms for query in self._queries)
            / len(self._queries)
        )

    def get_total_rows_affected(self) -> int:
        """
        Total rows affected across all queries.
        """

        return sum(
            query.rows_affected
            for query in self._queries
        )

    def clear(self):
        """
        Remove all stored queries.
        """
        self._queries.clear()

    def __len__(self):
        return len(self._queries)

    def __iter__(self):
        return iter(self._queries)

    def __str__(self):
        return (
            f"DatabaseQueryRepository("
            f"queries={len(self._queries)})"
        )
