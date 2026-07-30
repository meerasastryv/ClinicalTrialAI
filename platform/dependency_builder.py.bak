from platform.dependency_edge import DependencyEdge
from platform.dependency_graph import DependencyGraph
from platform.dependency_node import DependencyNode
from platform.dependency_resolver import DependencyResolver


class DependencyBuilder:

    def build(self, modules):

        graph = DependencyGraph()

        resolver = DependencyResolver(modules)

        # -----------------------------------------
        # Create graph nodes
        # -----------------------------------------

        for module in modules:

            graph.add_node(
                DependencyNode(
                    id=f"{module.ic_name}.{module.module_name}",
                    name=module.module_name,
                    module_type=module.module_type,
                    ic_name=module.ic_name,
                )
            )

        # -----------------------------------------
        # Create dependency edges
        # -----------------------------------------

        for module in modules:

            source = f"{module.ic_name}.{module.module_name}"

            for imp in module.imports:

                target = resolver.resolve(imp)

                if target:

                    graph.internal_imports += 1

                    graph.add_edge(
                        DependencyEdge(
                            source=source,
                            target=f"{target.ic_name}.{target.module_name}",
                        )
                    )

                else:

                    graph.external_imports += 1

        return graph
