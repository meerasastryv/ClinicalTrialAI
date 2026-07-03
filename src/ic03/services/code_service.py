
from ..repository.code_repository import CodeRepository
from ..models.code_model import CodeModel


class CodeService:
    """
    Service for managing the project's CodeModel.
    """

    def __init__(self):
        self.repository = CodeRepository()

    def load(self, code_model: CodeModel):
        self.repository.save(code_model)

    def get_code_model(self) -> CodeModel | None:
        return self.repository.get()
