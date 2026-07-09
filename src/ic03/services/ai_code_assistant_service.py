class AICodeAssistantService:
    """
    AI-oriented facade over the Code Intelligence Query Service.

    This service converts analysis results into natural-language
    explanations that can later be consumed by an LLM, REST API,
    chat interface, or UI.
    """

    def __init__(self, query_service):

        self.query = query_service

    # ---------------------------------------------------------
    # Project Summary
    # ---------------------------------------------------------

    def project_summary(self):
        """
        Returns the overall project summary.
        """

        return self.query.project_summary()

    # ---------------------------------------------------------
    # Architecture Summary
    # ---------------------------------------------------------

    def architecture_summary(self):
        """
        Returns architecture statistics.
        """

        return self.query.architecture_summary()

    # ---------------------------------------------------------
    # Health Summary
    # ---------------------------------------------------------

    def health_summary(self):
        """
        Returns overall architecture health.
        """

        return self.query.health_summary()

    # ---------------------------------------------------------
    # Platform Summary
    # ---------------------------------------------------------

    def platform_summary(self):
        """
        Returns a consolidated platform summary.
        """

        return self.query.summary()



    # ---------------------------------------------------------
    # Explain Component
    # ---------------------------------------------------------

    def explain_component(self, component):
        """
        Returns a natural-language explanation for a component.
        """

        incoming = self.query.incoming_relationships(component)
        outgoing = self.query.outgoing_relationships(component)

        explanation = []

        explanation.append(
            f"Component '{component}' participates in the project dependency graph."
        )

        explanation.append(
            f"It has {len(incoming)} incoming relationship(s)"
            f" and {len(outgoing)} outgoing relationship(s)."
        )

        if len(incoming) > len(outgoing):

            explanation.append(
                "The component is primarily depended upon by other components."
            )

        elif len(outgoing) > len(incoming):

            explanation.append(
                "The component depends on several other components."
            )

        else:

            explanation.append(
                "The component has a balanced dependency profile."
            )

        return " ".join(explanation)

    # ---------------------------------------------------------
    # Explain Impact
    # ---------------------------------------------------------

    def explain_impact(self, component):
        """
        Returns a natural-language impact analysis.
        """

        impact = self.query.impact_summary(component)

        return (
            f"Changing '{component}' may impact "
            f"{len(impact)} related component(s)."
        )

    # ---------------------------------------------------------
    # Search Components
    # ---------------------------------------------------------

    def search(self, keyword):
        """
        Searches the project for matching components.
        """

        return self.query.search_component(keyword)

    # ---------------------------------------------------------
    # Architecture Hotspots
    # ---------------------------------------------------------

    def architecture_hotspots(self):
        """
        Returns architecture hotspots.
        """

        return self.query.architecture_hotspots()

    # ---------------------------------------------------------
    # Circular Dependencies
    # ---------------------------------------------------------

    def circular_dependencies(self):
        """
        Returns circular dependencies.
        """

        return self.query.circular_dependencies()

    # ---------------------------------------------------------
    # Highly Coupled Components
    # ---------------------------------------------------------

    def highly_coupled_components(self):
        """
        Returns highly coupled components.
        """

        return self.query.highly_coupled_components()


    # ---------------------------------------------------------
    # Answer Question
    # ---------------------------------------------------------

    def answer(self, question):
        """
        Simple rule-based question router.
        This can later be replaced by an LLM.
        """

        q = question.lower()

        #
        # Architecture summary
        #
        if "architecture" in q and "summary" in q:

            return self._architecture_summary_text()

        #
        # Health
        #
        if "health" in q:

            return self._health_summary_text()

        #
        # Hotspots
        #
        if "hotspot" in q:

            return self._hotspots_text()

        #
        # Cycles
        #
        if "cycle" in q or "circular" in q:

            return self._cycles_text()

        #
        # Coupling
        #
        if "coupled" in q or "coupling" in q:

            return self._coupling_text()

        #
        # Default
        #
        return (
            "I could not understand the question. "
            "Supported topics include architecture, "
            "health, hotspots, cycles and coupling."
        )

    # ---------------------------------------------------------
    # Internal Response Builders
    # ---------------------------------------------------------

    def _architecture_summary_text(self):

        summary = self.architecture_summary()

        return (
            f"The architecture contains "
            f"{summary['components']} components, "
            f"{summary['relationships']} relationships, "
            f"{summary['cycles']} circular dependencies "
            f"and a stability index of "
            f"{summary['stability_index']}%."
        )

    def _health_summary_text(self):

        health = self.health_summary()

        return (
            f"Architecture Health Score: "
            f"{health['health_score']}%. "
            f"Stability Index: "
            f"{health['stability_index']}%."
        )

    def _hotspots_text(self):

        hotspots = self.architecture_hotspots()

        return (
            f"The project currently contains "
            f"{len(hotspots)} architecture hotspot(s)."
        )

    def _cycles_text(self):

        cycles = self.circular_dependencies()

        return (
            f"The dependency graph contains "
            f"{len(cycles)} circular dependency cycle(s)."
        )

    def _coupling_text(self):

        coupled = self.highly_coupled_components()

        return (
            f"The project contains "
            f"{len(coupled)} highly coupled component(s)."
        )



