from datetime import datetime


def filter_by_state(
    operations_data: list[dict[str, str | int]], state: str = "EXECUTED"
) -> list[dict[str, str | int]] | str:
    """Функция, которая фильтрует информацию по заданным критериям."""
    if not operations_data:
        return []
    elif state not in [operation.get("state") for operation in operations_data]:
        return "Состояние недействительно"
    return [operation for operation in operations_data if operation.get("state") == state]


def sort_by_date(operations_data: list[dict[str, str | int]], parameter: bool = True
                 ) -> list[dict[str, str | int]]:
    """Функция, которая возвращает новый список, отсортированный по дате"""
    for index, info in enumerate(operations_data):
        if info.get("date") is None:
            operations_data.pop(index)
            print(f"Дата операции {info.get("id")} неизвестна.")
        else:
            try:
                datetime.fromisoformat(str(info.get("date")))
            except ValueError:
                operations_data.pop(index)
                print(f"Дата операции {info.get("id")} должна быть в формате YYYY-MM-DD")
    return sorted(operations_data, key=lambda date: date["date"], reverse=parameter)
