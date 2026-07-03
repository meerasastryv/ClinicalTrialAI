from ..services.code_service import CodeService
from ..services.search_service import SearchService
from ..services.dependency_service import DependencyService

from ..models.code_model import CodeModel


def main():
    # -------------------------------
    # Code Service
    # -------------------------------
    code_service = CodeService()

    code_model = CodeModel(
        project_name="ClinicalTrialAI",
        source_files=[],
        modules=[],
        classes=[],
        functions=[]
    )

    code_service.load(code_model)

    print("\nCode Service")
    print("-" * 40)
    print(code_service.get_code_model())

    # -------------------------------
    # Search Service
    # -------------------------------
    search_service = SearchService()

    print("\nSearch Service")
    print("-" * 40)
    print("Functions:", search_service.get_functions())
    print("Methods:", search_service.get_methods())
    print("Class:", search_service.find_class("ProjectLoader"))

    # -------------------------------
    # Dependency Service
    # -------------------------------
    dependency_service = DependencyService()

    print("\nDependency Service")
    print("-" * 40)
    print("Dependencies:", dependency_service.get_dependencies())


if __name__ == "__main__":
    main()
