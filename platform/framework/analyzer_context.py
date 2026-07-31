"""
analyzer_context.py

Execution context shared by all analyzers.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict


@dataclass
class AnalyzerContext:
    """Runtime context supplied to analyzers."""

    project_root: Path

    output_dir: Path

    config: Dict[str, Any] = field(default_factory=dict)

    metadata: Dict[str, Any] = field(default_factory=dict)

    verbose: bool = False

    debug: bool = False

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
