"""
analyzer_descriptor.py

Metadata describing an analyzer.
"""

from dataclasses import dataclass


@dataclass
class AnalyzerDescriptor:

    name: str

    version: str = "1.0"

    description: str = ""

    author: str = "ClinicalTrialAI"

    enabled: bool = True
