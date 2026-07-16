"""
knowledge_report.py

Reporting module for knowledge evolution and maturity.
Generates formatted reports from the KnowledgeService.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.ic06.services.knowledge_service import KnowledgeService


class KnowledgeReport:
    """
    Generates reports for knowledge snapshots and evolution.
    """

    def __init__(
        self,
        knowledge_service: Optional[KnowledgeService] = None,
    ):
        self._knowledge_service = (
            knowledge_service or KnowledgeService()
        )

    # ------------------------------------------------------------------
    # Report Sections
    # ------------------------------------------------------------------

    def snapshot_summary(self) -> Dict:
        """
        Summary of stored knowledge snapshots.
        """
        snapshots = self._knowledge_service.get_all_snapshots()

        return {
            "total_snapshots": len(snapshots),
            "latest_snapshot": (
                self._knowledge_service.latest_snapshot()
            ),
        }

    def evolution(self) -> Dict:
        """
        Knowledge evolution history.
        """
        return {
            "history": self._knowledge_service.evolution()
        }

    def growth(self) -> Dict:
        """
        Knowledge growth metrics.
        """
        return self._knowledge_service.growth()

    def maturity(self) -> Dict:
        """
        Knowledge maturity metrics.
        """
        return {
            "maturity_score": (
                self._knowledge_service.maturity_score()
            )
        }

    # ------------------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------------------

    def executive_summary(self) -> Dict:
        """
        Executive summary of knowledge maturity.
        """

        maturity = (
            self._knowledge_service.maturity_score()
        )

        if maturity >= 0.80:
            status = "Excellent"
        elif maturity >= 0.70:
            status = "Healthy"
        elif maturity >= 0.50:
            status = "Developing"
        else:
            status = "Needs Improvement"

        return {
            "status": status,
            "maturity_score": maturity,
            "growth": self._knowledge_service.growth(),
        }

    # ------------------------------------------------------------------
    # Complete Report
    # ------------------------------------------------------------------

    def generate(self) -> Dict:
        """
        Generate the complete knowledge report.
        """

        return {
            "snapshot_summary": self.snapshot_summary(),
            "evolution": self.evolution(),
            "growth": self.growth(),
            "maturity": self.maturity(),
            "executive_summary": self.executive_summary(),
        }
