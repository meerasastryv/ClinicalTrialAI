"""
analysis_result.py

Common analysis result returned by all platform analyzers.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AnalysisResult:
    """Standard output of any analyzer."""

    analyzer_name: str

    success: bool = True

    summary: Dict[str, Any] = field(default_factory=dict)

    metrics: Dict[str, Any] = field(default_factory=dict)

    findings: List[Any] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)

    execution_time: float = 0.0

    generated_at: str = ""

    def add_finding(self, finding):
        self.findings.append(finding)

    def add_warning(self, warning: str):
        self.warnings.append(warning)

    def add_error(self, error: str):
        self.errors.append(error)
        self.success = False

    def add_metric(self, key: str, value: Any):
        self.metrics[key] = value

    def add_summary(self, key: str, value: Any):
        self.summary[key] = value

    def to_dict(self):
        return {
            "analyzer_name": self.analyzer_name,
            "success": self.success,
            "summary": self.summary,
            "metrics": self.metrics,
            "findings": self.findings,
            "warnings": self.warnings,
            "errors": self.errors,
            "metadata": self.metadata,
            "execution_time": self.execution_time,
            "generated_at": self.generated_at,
        }
