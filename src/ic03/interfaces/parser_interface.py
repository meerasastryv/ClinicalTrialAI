from abc import ABC, abstractmethod
from pathlib import Path
import ast


class ParserInterface(ABC):
    """
    Interface for all language parsers.
    """

    @abstractmethod
    def parse(self, file_path: Path) -> ast.Module:
        """
        Parse a source file into an AST.
        """
        pass
