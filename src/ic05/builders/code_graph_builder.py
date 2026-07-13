from src.ic05.services.graph_service import GraphService


class CodeGraphBuilder:
    """
    Builds a Knowledge Graph from IC-03 Code Intelligence artifacts.
    """

    def __init__(self):

        self.graph_service = GraphService()

    # ---------------------------------------------------------

    def build(
        self,
        class_repository,
    ):

        #
        # Pass 1
        # Create all Class nodes.
        #

        for class_model in class_repository.get_all_classes():

            self.add_class(class_model)

        #
        # Pass 2
        # Create Method nodes and CONTAINS relationships.
        #

        for class_model in class_repository.get_all_classes():

            self.add_methods(class_model)

        #
        # Pass 3
        # Create INHERITS relationships.
        #

        for class_model in class_repository.get_all_classes():

            self.add_inheritance(class_model)

        return self.graph_service

    # ---------------------------------------------------------

    def add_class(
        self,
        class_model,
    ):

        node = self.graph_service.add_node(
            node_id=class_model.name,
            node_type="Class",
            name=class_model.name,
        )

        node.source = "IC-03"

        node.add_label("Class")

        node.add_tag("Code")

        node.add_property(
            "Line Number",
            class_model.line_number,
        )

        node.add_property(
            "Docstring",
            class_model.docstring,
        )

        return node

    # ---------------------------------------------------------

    def add_methods(
        self,
        class_model,
    ):

        for method in class_model.methods:

            method_id = (
                f"{class_model.name}.{method.name}"
            )

            method_node = self.graph_service.add_node(
                node_id=method_id,
                node_type="Method",
                name=method.name,
            )

            method_node.source = "IC-03"

            method_node.add_label("Method")

            method_node.add_tag("Code")

            method_node.add_property(
                "Line Number",
                method.line_number,
            )

            method_node.add_property(
                "Docstring",
                method.docstring,
            )

            method_node.add_property(
                "Parameters",
                method.parameters,
            )

            method_node.add_property(
                "Decorators",
                method.decorators,
            )

            self.graph_service.add_edge(
                source=class_model.name,
                target=method_id,
                relationship="CONTAINS",
            )

    # ---------------------------------------------------------

    def add_inheritance(
        self,
        class_model,
    ):

        for base_class in class_model.base_classes:

            if self.graph_service.has_node(base_class):

                self.graph_service.add_edge(
                    source=class_model.name,
                    target=base_class,
                    relationship="INHERITS",
                )
