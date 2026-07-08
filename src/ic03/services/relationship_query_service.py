from collections import Counter

from src.ic03.repository.relationship_repository import (
    RelationshipRepository,
)

from src.ic03.models.relationship_type import (
    RelationshipType,
)


class RelationshipQueryService:
    """
    Provides high-level query APIs for RelationshipRepository.

    This service keeps the repository focused on persistence while
    exposing reusable queries for downstream intelligence engines.
    """

    def __init__(self, repository: RelationshipRepository):
        self.repository = repository

    # ---------------------------------------------------------
    # Basic Queries
    # ---------------------------------------------------------

    def get_all_relationships(self):
        return self.repository.get_all()

    def count_relationships(self):
        return self.repository.count()

    def relationship_exists(self, source, relationship_type, target):
        return any(
            r.source == source
            and r.relationship_type == relationship_type
            and r.target == target
            for r in self.repository.get_all()
        )

    # ---------------------------------------------------------
    # Type Queries
    # ---------------------------------------------------------

    def get_relationships_by_type(self, relationship_type):
        return self.repository.get_by_type(relationship_type)

    def get_method_calls(self):
        return self.get_relationships_by_type(
            RelationshipType.CALLS.value
        )

    def get_imports(self):
        return self.get_relationships_by_type(
            RelationshipType.IMPORTS.value
        )

    def get_inheritance_relationships(self):
        return self.get_relationships_by_type(
            RelationshipType.INHERITS.value
        )

    def get_class_dependencies(self):
        return self.get_relationships_by_type(
            RelationshipType.CLASS_DEPENDENCY.value
        )

    def get_file_dependencies(self):
        return self.get_relationships_by_type(
            RelationshipType.FILE_DEPENDENCY.value
        )

    # ---------------------------------------------------------
    # Graph Queries
    # ---------------------------------------------------------

    def get_outgoing_relationships(self, source):
        return self.repository.get_by_source(source)

    def get_incoming_relationships(self, target):
        return self.repository.get_by_target(target)

    def get_callers(self, callee):
        return [
            r.source
            for r in self.get_method_calls()
            if r.target == callee
        ]

    def get_callees(self, caller):
        return [
            r.target
            for r in self.get_method_calls()
            if r.source == caller
        ]

    # ---------------------------------------------------------
    # Inheritance Queries
    # ---------------------------------------------------------

    def get_parent_classes(self, child):
        return [
            r.target
            for r in self.get_inheritance_relationships()
            if r.source == child
        ]

    def get_child_classes(self, parent):
        return [
            r.source
            for r in self.get_inheritance_relationships()
            if r.target == parent
        ]

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def find_relationships(
        self,
        source=None,
        relationship_type=None,
        target=None,
    ):
        relationships = self.repository.get_all()

        if source is not None:
            relationships = [
                r for r in relationships if r.source == source
            ]

        if relationship_type is not None:
            relationships = [
                r
                for r in relationships
                if r.relationship_type == relationship_type
            ]

        if target is not None:
            relationships = [
                r for r in relationships if r.target == target
            ]

        return relationships

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def relationship_summary(self):
        counter = Counter(
            r.relationship_type
            for r in self.repository.get_all()
        )

        return dict(counter)

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    def print_summary(self):
        print("\nRelationship Summary")
        print("-" * 40)

        summary = self.relationship_summary()

        if not summary:
            print("No relationships discovered.")
            return

        for relationship_type in sorted(summary):
            print(
                f"{relationship_type:<25}"
                f"{summary[relationship_type]}"
            )
