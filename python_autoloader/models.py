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
    def from_module_name(
        cls,
        module_name: str,
        package: str = __package__,
    ) -> "PythonModule":
        """
        Create PythonModule from module name.

        :param module_name: Module name.
        :param package: Package name to allow relative imports. Defaults to the current package.
        :return: PythonModule.
        """
        module = importlib.import_module(module_name, package=package)
        name = module.__name__
        if name.endswith(".__init__"):
            name = name[:-9]
        return cls(name=name, module=module)

    def is_valid_file(self):
        return bool(self.module.__file__)

    def is_init_module(self):
        return self.module.__file__.endswith("__init__.py")


ValidateFunction = Callable[[Any], bool]
