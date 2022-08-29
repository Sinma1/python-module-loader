import importlib
import os
from dataclasses import dataclass
from types import ModuleType
from typing import Callable, Any


@dataclass
class PythonModule:
    """Wrapper for a python's module."""

    name: str
    module: ModuleType

    @property
    def directory(self):
        return os.path.dirname(self.module.__file__)

    def __str__(self):
        return f"{self.name} - {self.directory}"

    def __repr__(self):
        return f"{self.name} - {self.directory}"

    @classmethod
    def from_module_name(cls, module_name: str) -> "PythonModule":
        """
        Create PythonModule from module name.

        :param module_name: Module name.
        :return: PythonModule.
        """
        module = importlib.import_module(module_name)
        return cls(name=module_name, module=module)

    def is_valid_file(self):
        return bool(self.module.__file__)


ValidateFunction = Callable[[Any], bool]
