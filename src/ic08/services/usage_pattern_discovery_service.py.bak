"""
usage_pattern_discovery_service.py

Discovers customer usage patterns using DBSCAN clustering.
"""

from __future__ import annotations

import time
from typing import List, Optional

import numpy as np
from sklearn.base import TransformerMixin
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from src.ic08.models.discovery_result import (
    UsagePatternDiscoveryResult,
)
from src.ic08.models.feature_matrix import FeatureMatrix
from src.ic08.models.pattern_cluster import PatternCluster
from src.ic08.repositories.usage_pattern_repository import (
    UsagePatternRepository,
)


class UsagePatternDiscoveryService:
    """
    Performs machine learning clustering using DBSCAN.
    """

    def __init__(
        self,
        repository: UsagePatternRepository,
        eps: float = 0.5,
        min_samples: int = 3,
        scaler: Optional[TransformerMixin] = None,
    ) -> None:
        """
        Initialize the discovery service.
        """

        self._repository = repository

        self._eps = eps
        self._min_samples = min_samples

        self._scaler = scaler or StandardScaler()

        self._model = DBSCAN(
            eps=self._eps,
            min_samples=self._min_samples,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def discover_patterns(
        self,
        feature_matrix: FeatureMatrix,
    ) -> UsagePatternDiscoveryResult:
        """
        Execute the complete usage pattern discovery pipeline.
        """

        self._validate_feature_matrix(feature_matrix)

        start_time = time.perf_counter()

        labels = self._cluster(feature_matrix)

        clusters = self._build_pattern_clusters(
            feature_matrix.customer_ids,
            labels,
        )

        self._save_cluster_assignments(clusters)

        execution_time = (
            time.perf_counter() - start_time
        )

        return self._build_discovery_result(
            feature_matrix=feature_matrix,
            clusters=clusters,
            execution_time=execution_time,
        )

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate_feature_matrix(
        self,
        feature_matrix: FeatureMatrix,
    ) -> None:
        """
        Validate the supplied feature matrix.
        """

        if feature_matrix is None:
            raise ValueError(
                "Feature matrix cannot be None."
            )

        if feature_matrix.is_empty():
            raise ValueError(
                "Feature matrix is empty."
            )

    # ------------------------------------------------------------------
    # Machine Learning
    # ------------------------------------------------------------------

    def _cluster(
        self,
        feature_matrix: FeatureMatrix,
    ) -> List[int]:
        """
        Execute DBSCAN clustering.
        """

        x = np.array(
            feature_matrix.feature_values,
            dtype=float,
        )

        x_scaled = self._scaler.fit_transform(x)
        print()
        print("Scaled Feature Matrix")
        print(x_scaled)
        labels = self._model.fit_predict(
            x_scaled
        )
        print()
        print("DBSCAN labels:", labels)
        return labels.tolist()


    # ------------------------------------------------------------------
    # Cluster Construction
    # ------------------------------------------------------------------

    def _build_pattern_clusters(
        self,
        customer_ids: List[str],
        labels: List[int],
    ) -> List[PatternCluster]:
        """
        Convert cluster labels into PatternCluster objects.
        """

        clusters: List[PatternCluster] = []

        for customer_id, label in zip(
            customer_ids,
            labels,
        ):
            clusters.append(
                PatternCluster(
                    customer_id=customer_id,
                    cluster_id=label,
                    is_noise=(label == -1),
                    similarity_score=0.0,
                )
            )

        return clusters

    # ------------------------------------------------------------------
    # Repository
    # ------------------------------------------------------------------

    def _save_cluster_assignments(
        self,
        clusters: List[PatternCluster],
    ) -> None:
        """
        Persist cluster assignments.
        """

        for cluster in clusters:
            self._repository.save_cluster_assignment(
                cluster
            )

    # ------------------------------------------------------------------
    # Result Builder
    # ------------------------------------------------------------------

    def _build_discovery_result(
        self,
        feature_matrix: FeatureMatrix,
        clusters: List[PatternCluster],
        execution_time: float,
    ) -> UsagePatternDiscoveryResult:
        """
        Build the discovery result.
        """

        result = UsagePatternDiscoveryResult(
            algorithm="DBSCAN",
            eps=self._eps,
            min_samples=self._min_samples,
        )

        result.clusters = clusters

        result.customer_count = len(
            feature_matrix.customer_ids
        )

        result.feature_count = len(
            feature_matrix.feature_definitions
        )

        result.cluster_count = len(
            self._repository.get_cluster_ids()
        )

        result.noise_count = sum(
            1
            for cluster in clusters
            if cluster.is_noise
        )

        result.execution_time = execution_time

        return result
