from python_autoloader import helpers


def test_helpers():
    assert helpers.is_python_file("python_autoloader/helpers.py") is True
    assert helpers.is_python_file("python_autoloader/__init__.py") is True
    assert helpers.is_python_file("python_autoloader/loader.py") is True
    assert helpers.is_python_file("models.py") is True
    assert helpers.is_python_file("file") is False
    assert helpers.is_python_file("script.sh") is False
    assert helpers.is_python_file("file.pyc") is False
    assert helpers.is_python_file("") is False
    assert helpers.is_python_file(None) is False

