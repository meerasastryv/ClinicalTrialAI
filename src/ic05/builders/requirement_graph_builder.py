from src.ic05.services.graph_service import GraphService


class RequirementGraphBuilder:
    """
    Builds the Knowledge Graph from IC-01 Requirements.
    """

    def __init__(self):

        self.graph_service = GraphService()

    # ---------------------------------------------------------

    def build(
        self,
        requirements,
    ):

        # First create all Requirement nodes.
        for requirement in requirements:

            self.add_requirement(requirement)

        # Then create hierarchy relationships.
        for requirement in requirements:

            for parent_id in requirement.links:

                if self.graph_service.has_node(parent_id):

                    self.graph_service.add_edge(
                        source=parent_id,
                        target=requirement.id,
                        relationship="DERIVES_TO",
                    )

        return self.graph_service

    # ---------------------------------------------------------

    def add_requirement(
        self,
        requirement,
    ):

        node = self.graph_service.add_node(
            node_id=requirement.id,
            node_type="Requirement",
            name=requirement.text,
        )

        node.source = "IC-01"

        node.add_label(requirement.req_type)

        node.add_tag(requirement.product)

        node.add_tag("Requirements")

        node.add_property(
            "Product",
            requirement.product,
        )

        node.add_property(
            "Requirement Type",
            requirement.req_type,
        )

        return node
