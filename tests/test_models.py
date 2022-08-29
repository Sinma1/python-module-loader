import pytest

from python_autoloader.models import PythonModule


def test_python_module_model():
    python_module = PythonModule.from_module_name("python_autoloader.models")
    assert python_module.name == "python_autoloader.models"
    assert python_module.module.__file__.endswith("python_autoloader/models.py")
    assert python_module.directory.endswith("/python_autoloader")
    assert python_module.is_valid_file() is True
    assert python_module.is_init_module() is False

    python_module = PythonModule.from_module_name("tests.example")
    assert python_module.name == "tests.example"
    assert python_module.module.__file__.endswith("tests/example/__init__.py")
    assert python_module.directory.endswith("/tests/example")
    assert python_module.is_valid_file() is True
    assert python_module.is_init_module() is True

    python_module = PythonModule.from_module_name("tests.example.submodule")
    assert python_module.name == "tests.example.submodule"
    assert python_module.module.__file__.endswith("tests/example/submodule/__init__.py")
    assert python_module.directory.endswith("/tests/example/submodule")
    assert python_module.is_valid_file() is True
    assert python_module.is_init_module() is True

    python_module = PythonModule.from_module_name("tests.example.submodule.submodule1")
    assert python_module.name == "tests.example.submodule.submodule1"
    assert python_module.module.__file__.endswith(
        "tests/example/submodule/submodule1.py"
    )
    assert python_module.directory.endswith("/tests/example/submodule")
    assert python_module.is_valid_file() is True
    assert python_module.is_init_module() is False

    with pytest.raises(ModuleNotFoundError):
        PythonModule.from_module_name("tests.not_existing")

    with pytest.raises(ModuleNotFoundError):
        PythonModule.from_module_name("tests.example.not_existing")

    python_module = PythonModule.from_module_name(".")
    assert python_module.name == "python_autoloader"
    assert python_module.module.__file__.endswith("python_autoloader/__init__.py")
    assert python_module.directory.endswith("/python_autoloader")
    assert python_module.is_valid_file() is True
    assert python_module.is_init_module() is True

    python_module = PythonModule.from_module_name(".loader")
    assert python_module.name == "python_autoloader.loader"
    assert python_module.module.__file__.endswith("python_autoloader/loader.py")
    assert python_module.directory.endswith("/python_autoloader")
    assert python_module.is_valid_file() is True
    assert python_module.is_init_module() is False
