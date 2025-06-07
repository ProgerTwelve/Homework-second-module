import pytest

from src.decorators import log


@log()
def successful_func(a, b):
    return a + b


def test_log_success(capsys):
    successful_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "successful_func ok\n"


@log()
def failing_func(a, b):
    return a + b


def test_log_error(capsys):
    with pytest.raises(TypeError):
        failing_func("1", 2)
    captured = capsys.readouterr()
    assert "failing_func error: TypeError. Inputs: ('1', 2), {}\n" in captured.out
