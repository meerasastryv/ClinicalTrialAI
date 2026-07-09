class CodeIntelligenceQueryService:
    """
    Unified query interface for the IC-03 Code Intelligence Engine.
    Acts as a facade over all analysis services.
    """

    def __init__(
        self,
        relationship_query_service,
        graph_traversal_service,
        impact_analysis_service,
        architecture_metrics_service,
        advanced_architecture_service,
    ):

        self.relationship_query = relationship_query_service
        self.graph = graph_traversal_service
        self.impact = impact_analysis_service
        self.metrics = architecture_metrics_service
        self.architecture = advanced_architecture_service

    # ---------------------------------------------------------
    # Project Summary
    # ---------------------------------------------------------

    def project_summary(self):
        """
        Returns overall project statistics.
        """

        return {
            "nodes": self.metrics.get_node_count(),
            "relationships": self.metrics.get_edge_count(),
            "health_score": self.metrics.health_score(),
            "stability_index": self.architecture.stability_index(),
        }

    # ---------------------------------------------------------
    # Architecture Summary
    # ---------------------------------------------------------

    def architecture_summary(self):
        """
        Returns architecture statistics.
        """

        return self.architecture.detailed_summary()

    # ---------------------------------------------------------
    # Graph Statistics
    # ---------------------------------------------------------

    def graph_statistics(self):
        """
        Returns graph statistics.
        """

        return {
            "nodes": self.graph.node_count(),
            "edges": self.graph.edge_count(),
        }

    # ---------------------------------------------------------
    # Health Summary
    # ---------------------------------------------------------

    def health_summary(self):
        """
        Returns overall architecture health.
        """

        return {
            "health_score": self.metrics.health_score(),
            "stability_index": self.architecture.stability_index(),
        }



    # ---------------------------------------------------------
    # Architecture Hotspots
    # ---------------------------------------------------------

    def architecture_hotspots(self):
        """
        Returns architecture hotspots.
        """

        return self.metrics.hotspots()

    # ---------------------------------------------------------
    # Highly Coupled Components
    # ---------------------------------------------------------

    def highly_coupled_components(self):
        """
        Returns highly coupled components.
        """

        return self.architecture.highly_coupled_components()

    # ---------------------------------------------------------
    # Circular Dependencies
    # ---------------------------------------------------------

    def circular_dependencies(self):
        """
        Returns circular dependencies.
        """

        return self.architecture.detect_cycles()

    # ---------------------------------------------------------
    # Longest Dependency Chain
    # ---------------------------------------------------------

    def longest_dependency_chain(self):
        """
        Returns the longest dependency chain.
        """

        return self.architecture.longest_dependency_chain()

    # ---------------------------------------------------------
    # Architecture Smells
    # ---------------------------------------------------------

    def architecture_smells(self):
        """
        Returns architecture smells.
        """

        return self.architecture.architecture_smells()

    # ---------------------------------------------------------
    # Hub Components
    # ---------------------------------------------------------

    def hub_components(self):
        """
        Returns hub components.
        """

        return self.architecture.hub_components()

    # ---------------------------------------------------------
    # Orphan Components
    # ---------------------------------------------------------

    def orphan_components(self):
        """
        Returns orphan components.
        """

        return self.architecture.orphan_components()



    # ---------------------------------------------------------
    # Impact Analysis
    # ---------------------------------------------------------

    def impact_summary(self, component):
        """
        Returns impact analysis for a component.
        """

        return self.impact.impact_summary(component)

    # ---------------------------------------------------------
    # Dependency Path
    # ---------------------------------------------------------

    def dependency_path(self, source, destination):
        """
        Returns dependency path between two components.
        """

        return self.graph.shortest_path(
            source,
            destination
        )

    # ---------------------------------------------------------
    # Incoming Relationships
    # ---------------------------------------------------------

    def incoming_relationships(self, component):
        """
        Returns incoming relationships.
        """

        return self.relationship_query.get_incoming_relationships(
            component
        )

    # ---------------------------------------------------------
    # Outgoing Relationships
    # ---------------------------------------------------------

    def outgoing_relationships(self, component):
        """
        Returns outgoing relationships.
        """

        return self.relationship_query.get_outgoing_relationships(
            component
        )

    # ---------------------------------------------------------
    # Relationship Types
    # ---------------------------------------------------------

    def relationships_by_type(self, relationship_type):
        """
        Returns relationships filtered by type.
        """

        return self.relationship_query.get_relationships_by_type(
            relationship_type
        )

    # ---------------------------------------------------------
    # Search Component
    # ---------------------------------------------------------

    def search_component(self, keyword):
        """
        Searches graph nodes using a case-insensitive match.
        """

        keyword = keyword.lower()

        results = []

        for node in self.graph.get_nodes():

            if keyword in node.lower():

                results.append(node)

        return sorted(results)

    # ---------------------------------------------------------
    # Complete Summary
    # ---------------------------------------------------------

    def summary(self):
        """
        Returns a consolidated platform summary.
        """

        return {
            "project": self.project_summary(),
            "architecture": self.architecture_summary(),
            "graph": self.graph_statistics(),
            "health": self.health_summary(),
            "hotspots": len(self.architecture_hotspots()),
            "cycles": len(self.circular_dependencies()),
            "coupled_components": len(
                self.highly_coupled_components()
            ),
            "orphan_components": len(
                self.orphan_components()
            ),
        }
