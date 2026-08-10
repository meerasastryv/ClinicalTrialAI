"""
base_reporter.py

Base class for all report generators.
"""

import json
from abc import ABC, abstractmethod
from pathlib import Path

from .base_report import BaseReport


class BaseReporter(ABC):
    """
    Common functionality for report generation.
    """

    def __init__(self, output_dir):

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def build_report(self, analysis_result):
        """
        Convert AnalysisResult into BaseReport.
        """

    @abstractmethod
    def render_markdown(self, report: BaseReport):
        """
        Produce markdown representation.
        """

    def save_json(self, report: BaseReport, filename: str):

        path = self.output_dir / filename

        with open(path, "w", encoding="utf-8") as fp:
            json.dump(
                report.to_dict(),
                fp,
                indent=4,
                ensure_ascii=False,
            )

        return path

    def save_markdown(self, report: BaseReport, filename: str):

        path = self.output_dir / filename

        markdown = self.render_markdown(report)

        with open(path, "w", encoding="utf-8") as fp:
            fp.write(markdown)

        return path

    def generate(self, analysis_result, json_name, md_name):

        report = self.build_report(analysis_result)

        json_path = self.save_json(report, json_name)

        md_path = self.save_markdown(report, md_name)

        return report, json_path, md_path
