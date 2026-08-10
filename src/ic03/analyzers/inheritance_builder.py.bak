from collections import defaultdict

from src.ic03.models.class_model import ClassModel


class InheritanceBuilder:
    """
    Builds inheritance relationships between classes.
    """

    def __init__(self):
        self.parent_to_children = defaultdict(list)
        self.child_to_parents = defaultdict(list)

    def build(self, classes: list[ClassModel]):
        """
        Build inheritance maps from ClassModel objects.
        """

        self.parent_to_children.clear()
        self.child_to_parents.clear()

        for cls in classes:
            for parent in cls.base_classes:
                self.parent_to_children[parent].append(cls.name)
                self.child_to_parents[cls.name].append(parent)

    def get_children(self, parent_name: str) -> list[str]:
        """
        Return all child classes for a parent.
        """
        return self.parent_to_children.get(parent_name, [])

    def get_parents(self, child_name: str) -> list[str]:
        """
        Return all parent classes for a child.
        """
        return self.child_to_parents.get(child_name, [])

    def get_hierarchy(self) -> dict:
        """
        Return complete inheritance hierarchy.
        """
        return dict(self.parent_to_children)

    def print_hierarchy(self):
        """
        Print inheritance hierarchy.
        """

        if not self.parent_to_children:
            print("No inheritance relationships found.")
            return

        print("\nInheritance Hierarchy")
        print("-" * 40)

        for parent in sorted(self.parent_to_children):
            print(parent)

            for child in sorted(self.parent_to_children[parent]):
                print(f"   └── {child}")
