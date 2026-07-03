from ..repository.code_repository import CodeRepository
from ..models.code_model import CodeModel


def main():
    repo = CodeRepository()

    model = CodeModel(
        project_name="ClinicalTrialAI",
        source_files=[],
        modules=[],
        classes=[],
        functions=[],
    )

    repo.save(model)

    print("Stored:")
    print(repo.get())


if __name__ == "__main__":
    main()
