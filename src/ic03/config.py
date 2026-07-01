from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py": "Python",
}

IGNORE_DIRECTORIES = {
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "env",
    ".idea",
    ".vscode",
    "node_modules",
    "dist",
    "build",
}

DEFAULT_PROJECT_PATH = Path.cwd()
