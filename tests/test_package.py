import inspect

from python_autoloader import PythonAutoLoader


def test_python_autoloader():
    loader = PythonAutoLoader().load("tests.example")
    assert len(loader.modules) == 3

    classes = (
        PythonAutoLoader()
        .load("tests.example")
        .find_objects(validators=[inspect.isclass])
    )
    assert len(classes) == 2

    classes = (
        PythonAutoLoader()
        .load("tests.example", recursive=True)
        .find_objects(validators=[inspect.isclass])
    )
    assert len(classes) == 4
    assert {c.__name__ for c in classes} == {"A", "B", "C", "D"}
