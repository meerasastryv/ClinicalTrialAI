
from ..models.code_model import CodeModel


class CodeRepository:
    """
    Stores the complete project CodeModel.
    """

    def __init__(self):
        self.code_model: CodeModel | None = None

    def save(self, code_model: CodeModel):
        self.code_model = code_model

    def get(self) -> CodeModel | None:
        return self.code_model
