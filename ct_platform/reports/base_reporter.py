"""
Base reporting framework.

Provides reusable report generation utilities for all ClinicalTrialAI
Intelligence Components.

Supported formats:
- Markdown
- JSON
- CSV

Author: ClinicalTrialAI
"""

from __future__ import annotations

import csv
import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


class BaseReporter(ABC):
    """
    Abstract base class for all report generators.

    Derived reporters only need to implement build_report().
    """

    def __init__(self, output_directory: str | Path = "reports") -> None:
        """
        Initialize reporter.

        Parameters
        ----------
        output_directory:
            Directory where reports will be generated.
        """
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def build_report(self, *args: Any, **kwargs: Any) -> Any:
        """
        Build report data.

        Returns
        -------
        Any
            Report representation suitable for the derived reporter.
        """
        raise NotImplementedError

    def generate_timestamp(self) -> str:
        """
        Generate timestamp for filenames.

        Returns
        -------
        str
        """
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def build_output_path(
        self,
        filename: str,
        extension: str,
    ) -> Path:
        """
        Build output file path.

        Parameters
        ----------
        filename:
            Base filename.

        extension:
            File extension.

        Returns
        -------
        Path
        """
        return self.output_directory / f"{filename}.{extension}"

    def write_markdown(
        self,
        filename: str,
        content: str,
    ) -> Path:
        """
        Write Markdown report.

        Parameters
        ----------
        filename:
            Output filename without extension.

        content:
            Markdown content.

        Returns
        -------
        Path
            Generated report path.
        """
        path = self.build_output_path(filename, "md")

        path.write_text(
            content,
            encoding="utf-8",
        )

        logger.info("Markdown report written: %s", path)

        return path

    def write_json(
        self,
        filename: str,
        data: Any,
        indent: int = 4,
    ) -> Path:
        """
        Write JSON report.

        Parameters
        ----------
        filename:
            Output filename.

        data:
            Serializable object.

        indent:
            JSON indentation.

        Returns
        -------
        Path
        """
        path = self.build_output_path(filename, "json")

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=indent,
                ensure_ascii=False,
            )

        logger.info("JSON report written: %s", path)

        return path

    def write_csv(
        self,
        filename: str,
        rows: list[dict[str, Any]],
    ) -> Path:
        """
        Write CSV report.

        Parameters
        ----------
        filename:
            Output filename.

        rows:
            List of dictionaries.

        Returns
        -------
        Path
        """
        path = self.build_output_path(filename, "csv")

        if not rows:
            with path.open(
                "w",
                newline="",
                encoding="utf-8",
            ):
                pass

            logger.info("Empty CSV report written: %s", path)
            return path

        fieldnames = list(rows[0].keys())

        with path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for row in rows:
                writer.writerow(row)

        logger.info("CSV report written: %s", path)

        return path
