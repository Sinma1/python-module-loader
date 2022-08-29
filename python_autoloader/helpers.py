import logging


def get_logger() -> logging.Logger:
    """Get logger for PythonAutoloader."""
    return logging.getLogger("PythonAutoloader")


def is_python_file(file: str) -> bool:
    """Check if file is a python file by checking its extension."""
    return file.endswith(".py")
