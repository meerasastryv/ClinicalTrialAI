from collections import defaultdict

from src.ic03.models.relationship import Relationship


class RelationshipRepository:
    """
    Stores relationships discovered during code analysis.
    """

    def __init__(self):
        self.relationships = []

    def add_relationship(self, relationship: Relationship):
        self.relationships.append(relationship)

    def get_all(self):
        return self.relationships

    def get_by_source(self, source: str):
        return [
            relationship
            for relationship in self.relationships
            if relationship.source == source
        ]

    def get_by_target(self, target: str):
        return [
            relationship
            for relationship in self.relationships
            if relationship.target == target
        ]

    def get_by_type(self, relationship_type: str):
        return [
            relationship
            for relationship in self.relationships
            if relationship.relationship_type == relationship_type
        ]

    def clear(self):
        self.relationships.clear()

    def count(self):
        return len(self.relationships)
