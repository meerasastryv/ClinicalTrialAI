import ast
from pathlib import Path


from src.ic03.interfaces.parser_interface import ParserInterface


class PythonASTParser(ParserInterface):
    """Parses Python source files into an Abstract Syntax Tree (AST)."""
    def parse(self, file_path: Path) -> ast.Module:
        """
        Parse a Python source file and return its AST.

        Args:
            file_path: Path to the Python source file.

        Returns:
            ast.AST: Parsed Abstract Syntax Tree.

        Raises:
            SyntaxError: If the source file contains invalid Python syntax.
            OSError: If the file cannot be read.
        """

        source = file_path.read_text(encoding="utf-8")

        return ast.parse(source, filename=str(file_path))
