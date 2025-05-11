import pytest

from src.decorators import log


@log(filename=None)
def my_function(x, y):
    """Тестовая функция с декоратором"""
    return x / y


def test_decorator_log():
    """Тестирование декоратора без выхода ошибки"""
    @log(filename=None)
    def my_function_(x, y):
        return x / y
    assert my_function(6, 3) == 2


def test_decorator_log_error():
    """Тестирование декоратора с выходом ошибки"""
    with pytest.raises(Exception):
        my_function(6, 0)


def test_decorator_cupsys(capsys):
    """Тестирование декоратора с выходом ошибки с фикстурой cupsys"""
    with pytest.raises(Exception):
        my_function()
        captured = my_function.readouterr()
        assert captured.out == Exception
