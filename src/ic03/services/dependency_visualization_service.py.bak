from pathlib import Path

from src.ic03.models.relationship_type import RelationshipType


class DependencyVisualizationService:
    """
    Generates Graphviz DOT files for the discovered relationships.
    """

    def __init__(self, relationship_repository):

        self.relationship_repository = relationship_repository

        self.output_dir = Path("reports")
        self.output_dir.mkdir(exist_ok=True)

    # ---------------------------------------------------------
    # Internal Helper
    # ---------------------------------------------------------

    def _write_dot_file(
        self,
        filename,
        title,
        edges,
        rankdir="LR"
    ):
        """
        Writes a Graphviz DOT file.
        """

        output_file = self.output_dir / filename

        with open(output_file, "w", encoding="utf-8") as f:

            f.write(f'digraph "{title}" {{\n')
            f.write(f'    rankdir={rankdir};\n')
            f.write("    node [shape=box];\n\n")

            for source, target in sorted(edges):
                f.write(f'    "{source}" -> "{target}";\n')

            f.write("}\n")

        return output_file

    # ---------------------------------------------------------
    # Module Dependency Graph
    # ---------------------------------------------------------

    def export_module_graph(self):
        """
        Export module dependency graph.
        """

        edges = set()

        for relationship in self.relationship_repository.get_all():

            if relationship.relationship_type != RelationshipType.IMPORTS.value:
                continue

            if relationship.source == relationship.target:
                continue

            edges.add(
                (
                    relationship.source,
                    relationship.target
                )
            )

        output_file = self._write_dot_file(
            filename="dependency_graph.dot",
            title="Module Dependency Graph",
            edges=edges
        )

        print(
            f"[Visualization] Module graph exported -> {output_file}"
        )

        return output_file

    # ---------------------------------------------------------
    # Method Call Graph
    # ---------------------------------------------------------

    def export_method_call_graph(self):
        """
        Export method call graph.
        """

        edges = set()

        for relationship in self.relationship_repository.get_all():

            if relationship.relationship_type != RelationshipType.CALLS.value:
                continue

            if relationship.source == relationship.target:
                continue

            edges.add(
                (
                    relationship.source,
                    relationship.target
                )
            )

        output_file = self._write_dot_file(
            filename="method_call_graph.dot",
            title="Method Call Graph",
            edges=edges
        )

        print(
            f"[Visualization] Method call graph exported -> {output_file}"
        )

        return output_file

    # ---------------------------------------------------------
    # Inheritance Graph
    # ---------------------------------------------------------

    def export_inheritance_graph(self):
        """
        Export inheritance graph.
        """

        edges = set()

        for relationship in self.relationship_repository.get_all():

            if relationship.relationship_type != RelationshipType.INHERITS.value:
                continue

            if relationship.source == relationship.target:
                continue

            edges.add(
                (
                    relationship.source,
                    relationship.target
                )
            )

        output_file = self._write_dot_file(
            filename="inheritance_graph.dot",
            title="Inheritance Graph",
            edges=edges
        )

        print(
            f"[Visualization] Inheritance graph exported -> {output_file}"
        )

        return output_file

    # ---------------------------------------------------------
    # Complete Relationship Graph
    # ---------------------------------------------------------

    def export_relationship_graph(self):
        """
        Export complete relationship graph.
        """

        edges = set()

        for relationship in self.relationship_repository.get_all():

            if relationship.source == relationship.target:
                continue

            edges.add(
                (
                    relationship.source,
                    relationship.target
                )
            )

        output_file = self._write_dot_file(
            filename="relationship_graph.dot",
            title="Relationship Graph",
            edges=edges
        )

        print(
            f"[Visualization] Relationship graph exported -> {output_file}"
        )

        return output_file

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def generate_summary(self):
        """
        Print visualization summary.
        """

        relationships = self.relationship_repository.get_all()

        imports = sum(
            1
            for relationship in relationships
            if relationship.relationship_type == RelationshipType.IMPORTS.value
        )

        calls = sum(
            1
            for relationship in relationships
            if relationship.relationship_type == RelationshipType.CALLS.value
        )

        inheritance = sum(
            1
            for relationship in relationships
            if relationship.relationship_type == RelationshipType.INHERITS.value
        )

        print("\n========================================")
        print("DEPENDENCY VISUALIZATION SUMMARY")
        print("========================================")
        print(f"Import Relationships      : {imports}")
        print(f"Method Calls              : {calls}")
        print(f"Inheritance Relationships : {inheritance}")
        print(f"Total Relationships       : {len(relationships)}")
        print("========================================")

    # ---------------------------------------------------------
    # Export Everything
    # ---------------------------------------------------------

    def export_all(self):
        """
        Export all visualization graphs.
        """

        print("\nGenerating dependency visualization...")

        self.export_module_graph()
        self.export_method_call_graph()
        self.export_inheritance_graph()
        self.export_relationship_graph()

        self.generate_summary()

        print("\nDependency visualization completed.\n")
