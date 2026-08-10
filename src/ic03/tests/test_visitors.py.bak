from pathlib import Path
from src.ic03.visitors.import_visitor import ImportVisitor
from src.ic03.visitors.class_visitor import ClassVisitor
from src.ic03.visitors.function_visitor import FunctionVisitor
from src.ic03.visitors.method_visitor import MethodVisitor
from src.ic03.parsers.python_ast_parser import PythonASTParser
from src.ic03.builders.method_builder import MethodBuilder
from ..builders.class_builder import ClassBuilder
from ..builders.function_builder import FunctionBuilder
from src.ic03.builders.code_builder import CodeModelBuilder
from src.ic03.builders.module_builder import ModuleBuilder

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
    # Function Builder
    function_builder = FunctionBuilder()
    print("\nFunction Models")
    print("-" * 40)
    for function in function_visitor.functions:
        model = function_builder.build_function(function)
        function_models.append(model)
        print(model)
    # Method Visitor
    method_visitor = MethodVisitor()
    method_visitor.visit(tree)
    print("\nMethods Found")
    print("-" * 40)
    for class_name, methods in method_visitor.methods.items():
        print(f"\nClass: {class_name}")
        for method in methods:
            print(method)
    builder = MethodBuilder()
    print("\nMethod Models")
    print("-" * 40)
    for class_name, methods in method_visitor.methods.items():
        print(f"\nClass : {class_name}")
        for method in methods:
            model = builder.build_method(method)
            print(model)
    class_builder = ClassBuilder()
    print("\nClass Models")
    print("-" * 40)
    class_models = []
    for cls in class_visitor.classes:
        model = class_builder.build_class(cls)
        class_models.append(model)
        print(model)
    module_builder = ModuleBuilder()
    module_model = module_builder.build_module(
                   name="project_loader",
                   imports=sorted(import_visitor.imports),
                   classes=[class_builder.build_class(cls)
                            for cls in class_visitor.classes],
                            functions=[function_builder.build_function(fn)
                                      for fn in function_visitor.functions ],
                            path="src/ic03/project_loader.py",)
    print("\nModule Model")
    print("-" * 40)
    print(module_model)

    code_builder = CodeModelBuilder()

    code_model = code_builder.build_code(project_name="ClinicalTrialAI",source_files=["src/ic03/project_loader.py"],
                                              modules=[module_model],classes=[class_builder.build_class(cls)for cls in class_visitor.classes],
    functions=[function_builder.build_function(fn)
		 for fn in function_visitor.functions ],)
    print("\nCode Model")
    print("-" * 40)
    print(code_model)





if __name__ == "__main__":
    main()
