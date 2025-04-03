import pytest

# Тестируемый декоратор
from decorators.log import log


# Тестовая функция без ошибок
@log()
def add(a, b):
    return a + b


# Тестовая функция с ошибкой
@log()
def divide(a, b):
    return a / b


# Тестовая функция с ключевыми аргументами
@log()
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def test_log_success(capsys):
    """Тест успешного выполнения функции"""
    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert captured.out == "add ok\n"


def test_log_error(capsys):
    """Тест обработки ошибки в функции"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0), {}" in captured.out


def test_log_with_keyword_args(capsys):
    """Тест функции с ключевыми аргументами"""
    result = greet("Alice", greeting="Hi")
    captured = capsys.readouterr()

    assert result == "Hi, Alice!"
    assert captured.out == "greet ok\n"


def test_log_with_file(tmp_path):
    """Тест записи в файл с использованием встроенной фикстуры tmp_path"""
    test_filename = tmp_path / "test_log.txt"

    @log(filename=str(test_filename))
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)

    assert result == 12
    assert test_filename.read_text() == "multiply ok\n"


def test_log_error_with_file(tmp_path):
    """Тест обработки ошибки с записью в файл"""
    test_filename = tmp_path / "test_error_log.txt"

    @log(filename=str(test_filename))
    def faulty_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        faulty_func()

    content = test_filename.read_text()
    assert "faulty_func error: ValueError" in content
    assert "Inputs: (), {}" in content
