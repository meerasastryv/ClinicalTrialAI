from ..models.code_model import CodeModel


class CodeModelBuilder:
    """
    Builds a CodeModel representing the entire source code project.
    """

    def build_code(self,
                   project_name: str,
                   source_files: list,
                   modules: list,
                   classes: list,
                   functions: list) -> CodeModel:

        return CodeModel(
            project_name=project_name,
            source_files=source_files,
            modules=modules,
            classes=classes,
            functions=functions,
        )
