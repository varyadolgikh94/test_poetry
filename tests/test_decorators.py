import tempfile

from src.decorators import log


def test_log_good_file_log():
    """Проверяет записи в файле после успешного выполнения функции."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "func ok" in logs


def test_log_bad_file_log():
    """Проверяет записи в файле после ошибки."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def error_func():
        raise ValueError("Что-то пошло не так!")

    error_func()

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "error_func error: Что-то пошло не так!. Inputs: (), {}" in logs


def test_log_good_console_log(capsys):
    """Тестовый вывод на консоль после успешного выполнения функции."""

    @log()
    def func(x, y):
        return x + y

    func(1, 2)
    captured = capsys.readouterr()

    assert "func ok\n" in captured.out


def test_log_bad_console_log(capsys):
    """Тестовый вывод на консоль после ошибки."""

    @log()
    def error_func():
        raise ValueError("Что-то пошло не так!")

    error_func()
    captured = capsys.readouterr()

    assert "error_func error: Что-то пошло не так!. Inputs: (), {}\n" in captured.out