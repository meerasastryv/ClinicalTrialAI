from ..project_loader import ProjectLoader
from ..file_scanner import FileScanner
from ..parsers.python_ast_parser import PythonASTParser

from ..visitors.import_visitor import ImportVisitor
from ..visitors.class_visitor import ClassVisitor
from ..visitors.function_visitor import FunctionVisitor
from ..visitors.method_visitor import MethodVisitor

from ..builders.method_builder import MethodBuilder
from ..builders.function_builder import FunctionBuilder
from ..builders.class_builder import ClassBuilder
from ..builders.module_builder import ModuleBuilder
from ..builders.code_builder import CodeModelBuilder

from ..repository.code_repository import CodeRepository
from ..repository.module_repository import ModuleRepository
from ..repository.class_repository import ClassRepository
from ..repository.function_repository import FunctionRepository
from ..repository.method_repository import MethodRepository


class ProjectAnalysisService:

    def __init__(self):

        self.parser = PythonASTParser()

        self.method_builder = MethodBuilder()
        self.function_builder = FunctionBuilder()
        self.class_builder = ClassBuilder()
        self.module_builder = ModuleBuilder()
        self.code_builder = CodeModelBuilder()

        self.code_repository = CodeRepository()
        self.module_repository = ModuleRepository()
        self.class_repository = ClassRepository()
        self.function_repository = FunctionRepository()
        self.method_repository = MethodRepository()

    def analyze(self, project_path):

        loader = ProjectLoader(project_path)
        root = loader.get_project_root()

        scanner = FileScanner(root)
        source_files = scanner.scan()

        #
        # Process every source file
        #
        for source_file in source_files:

            tree = self.parser.parse(source_file.path)

            # -------------------------------------------------
            # Visitors
            # -------------------------------------------------
            import_visitor = ImportVisitor(str(source_file.path))
            # import_visitor = ImportVisitor()
            class_visitor = ClassVisitor()
            function_visitor = FunctionVisitor()
            method_visitor = MethodVisitor()

            import_visitor.visit(tree)
            class_visitor.visit(tree)
            function_visitor.visit(tree)
            method_visitor.visit(tree)

            # -------------------------------------------------
            # Method Models
            # -------------------------------------------------

            method_models = []

            for methods in method_visitor.methods.values():
                for method in methods:
                    model = self.method_builder.build_method(method)
                    method_models.append(model)

            # -------------------------------------------------
            # Function Models
            # -------------------------------------------------

            function_models = []

            for function in function_visitor.functions:
                model = self.function_builder.build_function(function)
                function_models.append(model)

            # -------------------------------------------------
            # Class Models
            # -------------------------------------------------

            class_models = []

            for cls in class_visitor.classes:
                model = self.class_builder.build_class(cls)
                class_models.append(model)

            # -------------------------------------------------
            # Module Model
            # -------------------------------------------------

            module_model = self.module_builder.build_module(
                source_file.path,
                import_visitor.imports,
                class_models,
                function_models
            )

            # -------------------------------------------------
            # Save into repositories
            # -------------------------------------------------


            self.module_repository.add(module_model)
            for model in class_models:
                self.class_repository.add(model)
            for model in function_models:
                self.function_repository.add(model)

            for model in method_models:
                self.method_repository.add(model)

        #
        # Build Code Model
        #

        code_model = self.code_builder.build_code(
            project_name=root.name,
            source_files=source_files,
            modules=self.module_repository.get_all(),
            classes=self.class_repository.get_all(),
            functions=self.function_repository.get_all()
        )

        self.code_repository.save(code_model)

        return code_model
