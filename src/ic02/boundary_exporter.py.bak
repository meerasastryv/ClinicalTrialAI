"""
boundary_exporter.py

Exports Boundary Analysis results to JSON.

Author: Meera Sastry
Project: ClinicalTrialAI - IC-02 Test Design Engine
"""

import json
from dataclasses import asdict
from pathlib import Path

from boundary_models import BoundaryAnalysisResult


class BoundaryExporter:
    """
    Exports BoundaryAnalysisResult to JSON.
    """

    def export_to_json(
        self,
        result: BoundaryAnalysisResult,
        output_file: str
    ) -> None:

        data = asdict(result)

        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"\nJSON exported successfully to:\n{output_path}")
