from pathlib import Path
from visitors.class_visitor import ClassVisitor
from parsers.python_ast_parser import PythonASTParser
from visitors.import_visitor import ImportVisitor
parser = PythonASTParser()

#tree = parser.parse(Path("src/ic03/main.py"))
tree = parser.parse(Path("src/ic03/project_loader.py"))
visitor = ImportVisitor()
visitor.visit(tree)
print("\nImports Found")
print("-" * 40)
for item in visitor.imports:
    print(item)
class_visitor = ClassVisitor()
class_visitor.visit(tree)
print("\nClasses Found")
print("-" * 40)

for cls in class_visitor.classes:
    print(cls)
from visitors.function_visitor import FunctionVisitor
function_visitor = FunctionVisitor()
function_visitor.visit(tree)
print("\nFunctions Found")
print("-" * 40)
for function in function_visitor.functions:
    print(function)

from visitors.method_visitor import MethodVisitor

method_visitor = MethodVisitor()

method_visitor.visit(tree)

print("\nMethods Found")
print("-" * 40)

for cls, methods in method_visitor.methods.items():

    print(f"\nClass : {cls}")

    for method in methods:
        print(method)
