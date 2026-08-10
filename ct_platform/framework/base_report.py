"""
base_report.py

Base report model shared by all platform analyzers.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class BaseReport:
    """
    Base class for all analyzer reports.
    """

    report_name: str = ""

    analyzer_name: str = ""

    generated_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    summary: Dict[str, Any] = field(default_factory=dict)

    metrics: Dict[str, Any] = field(default_factory=dict)

    metadata: Dict[str, Any] = field(default_factory=dict)

    sections: Dict[str, Any] = field(default_factory=dict)

    def add_section(self, name: str, content):

        self.sections[name] = content

    def add_metric(self, name: str, value):

        self.metrics[name] = value

    def add_summary(self, name: str, value):

        self.summary[name] = value

    def to_dict(self):

        return {
            "report_name": self.report_name,
            "analyzer_name": self.analyzer_name,
            "generated_at": self.generated_at,
            "summary": self.summary,
            "metrics": self.metrics,
            "metadata": self.metadata,
            "sections": self.sections,
        }
