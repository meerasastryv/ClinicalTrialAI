from project_loader import ProjectLoader
from file_scanner import FileScanner


def main():

    project = input("Enter project path: ").strip()

    loader = ProjectLoader(project)
    project_root = loader.get_project_root()

    scanner = FileScanner(project_root)
    files = scanner.scan()

    print("\nProject Loaded Successfully")
    print("-" * 60)
    print(f"Files Found : {len(files)}")
    print("-" * 60)

    for file in files:
        print(f"{file.language:<10} {file.relative_path}")

    print("-" * 60)
    print(f"Total Files : {len(files)}")


if __name__ == "__main__":
    main()
