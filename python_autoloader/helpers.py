import logging


def get_logger() -> logging.Logger:
    """Get logger for PythonAutoloader."""
    return logging.getLogger("PythonAutoloader")


def is_python_file(file_name: str) -> bool:
    """Check if file_name is a python file by checking its extension."""
    return file_name.endswith(".py") if file_name else False
