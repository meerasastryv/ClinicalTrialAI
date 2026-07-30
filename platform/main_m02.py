from platform.dependency_builder import DependencyBuilder
from platform.dependency_inspector import DependencyInspector


def main():

    inspector = DependencyInspector()

    modules = inspector.scan()

    builder = DependencyBuilder()

    graph = builder.build(modules)

    print("=" * 70)
    print("ClinicalTrialAI Dependency Graph")
    print("=" * 70)

    print()

    print(f"Modules           : {graph.node_count()}")
    print(f"Edges             : {graph.edge_count()}")
    print(f"Internal Imports  : {graph.internal_imports}")
    print(f"External Imports  : {graph.external_imports}")

if __name__ == "__main__":
    main()
