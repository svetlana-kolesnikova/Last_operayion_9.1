from typing import Any

from src.decorators import log


@log(filename=None)
def my_function(x: int, y: int) -> float:
    """Тестовая функция с декоратором"""
    return x / y


def test_decorator_log() -> Any:
    """Тестирование декоратора без выхода ошибки"""

    @log(filename=None)
    def my_function_(x: int, y: int) -> float:
        return x / y

    assert my_function_(6, 3) == 2


def test_decorator_cupsys_2(capsys: Any) -> Any:
    """Тестирование декоратора без выхода ошибки с фикстурой cupsys"""
    my_function(6, 3)
    captured = capsys.readouterr()
    assert "ok" in captured.out


def test_decorator_log_in_file() -> Any:
    """Тестирование декоратора без выхода ошибки"""

    @log(filename="test_log.log")
    def my_function_(x: int, y: int) -> Any:
        return x / y

    assert my_function_(6, 3) == 2
    with open("test_log.log", encoding="utf-8") as f:
        data = f.read().split("\n")[:-1]
    assert data[-1] == "my_function_ ok"


def test_decorator_log_error_in_file() -> Any:
    """Тестирование декоратора выходом ошибки"""

    @log(filename="test_log.log")
    def my_function_(x: int, y: int) -> Any:
        return x / y

    my_function_(6, 0)
    with open("test_log.log", encoding="utf-8") as f:
        data = f.read().split("\n")[:-1]
    assert data[-1] == "my_function_ error: division by zero. Inputs: (6, 0), {}"
