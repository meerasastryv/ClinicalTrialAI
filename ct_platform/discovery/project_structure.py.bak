"""
Project structure models.

Represents the hierarchical directory and file structure discovered by
the Platform Discovery Engine.

Author: ClinicalTrialAI
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator


@dataclass(slots=True)
class ProjectNode:
    """
    Represents a file or directory in the project tree.
    """

    name: str
    path: Path
    is_directory: bool

    parent: ProjectNode | None = None
    children: list["ProjectNode"] = field(default_factory=list)

    def add_child(self, child: "ProjectNode") -> None:
        """
        Add a child node.

        Parameters
        ----------
        child
            Child node to add.
        """
        child.parent = self
        self.children.append(child)

    def find_child(self, name: str) -> "ProjectNode | None":
        """
        Find a direct child by name.

        Parameters
        ----------
        name
            Child node name.

        Returns
        -------
        ProjectNode | None
        """
        for child in self.children:
            if child.name == name:
                return child

        return None

    def walk(self) -> Iterator["ProjectNode"]:
        """
        Depth-first traversal beginning with this node.

        Yields
        ------
        ProjectNode
        """
        yield self

        for child in self.children:
            yield from child.walk()

    @property
    def depth(self) -> int:
        """
        Return the depth of this node.

        Root node depth is zero.
        """
        depth = 0
        current = self.parent

        while current is not None:
            depth += 1
            current = current.parent

        return depth

    @property
    def is_leaf(self) -> bool:
        """
        Return True if this node has no children.
        """
        return len(self.children) == 0

    def to_dict(self) -> dict[str, object]:
        """
        Convert this node to a serializable dictionary.
        """
        return {
            "name": self.name,
            "path": str(self.path),
            "is_directory": self.is_directory,
            "children": [
                child.to_dict()
                for child in self.children
            ],
        }


@dataclass(slots=True)
class ProjectStructure:
    """
    Represents the discovered project hierarchy.
    """

    root: ProjectNode

    def walk(self) -> Iterator[ProjectNode]:
        """
        Traverse the complete project tree.

        Yields
        ------
        ProjectNode
        """
        yield from self.root.walk()

    def find_node(self, path: Path) -> ProjectNode | None:
        """
        Find a node by path.

        Parameters
        ----------
        path
            Absolute or project-relative path.

        Returns
        -------
        ProjectNode | None
        """
        target = path.resolve()

        for node in self.walk():
            try:
                if node.path.resolve() == target:
                    return node
            except FileNotFoundError:
                if node.path == path:
                    return node

        return None

    @property
    def total_nodes(self) -> int:
        """
        Total number of nodes.
        """
        return sum(1 for _ in self.walk())

    @property
    def total_directories(self) -> int:
        """
        Total number of directories.
        """
        return sum(
            1
            for node in self.walk()
            if node.is_directory
        )

    @property
    def total_files(self) -> int:
        """
        Total number of files.
        """
        return sum(
            1
            for node in self.walk()
            if not node.is_directory
        )

    def to_dict(self) -> dict[str, object]:
        """
        Convert the entire structure to a serializable dictionary.
        """
        return self.root.to_dict()
