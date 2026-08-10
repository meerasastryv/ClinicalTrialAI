from datetime import datetime


def format_size(size: int) -> str:
    """Return human-readable file size."""

    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} TB"


def format_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")
