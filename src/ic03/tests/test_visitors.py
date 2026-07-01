from pathlib import Path

from parsers.python_ast_parser import PythonASTParser
from visitors.import_visitor import ImportVisitor
from visitors.class_visitor import ClassVisitor
from visitors.function_visitor import FunctionVisitor
from visitors.method_visitor import MethodVisitor


def main():

    parser = PythonASTParser()

    tree = parser.parse(Path("src/ic03/project_loader.py"))

    # Import Visitor
    import_visitor = ImportVisitor()
    import_visitor.visit(tree)

    print("\nImports Found")
    print("-" * 40)
    for item in sorted(import_visitor.imports):
        print(item)

    # Class Visitor
    class_visitor = ClassVisitor()
    class_visitor.visit(tree)

    print("\nClasses Found")
    print("-" * 40)
    for cls in class_visitor.classes:
        print(cls)

    # Function Visitor
    function_visitor = FunctionVisitor()
    function_visitor.visit(tree)

    print("\nFunctions Found")
    print("-" * 40)
    for function in function_visitor.functions:
        print(function)

    # Method Visitor
    method_visitor = MethodVisitor()
    method_visitor.visit(tree)

    print("\nMethods Found")
    print("-" * 40)
    for class_name, methods in method_visitor.methods.items():
        print(f"\nClass: {class_name}")
        for method in methods:
            print(method)


if __name__ == "__main__":
    main()
