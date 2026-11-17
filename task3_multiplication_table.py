"""Задание 3. Таблица умножения для числа от 1 до 10."""

from __future__ import annotations

from collections.abc import Callable

from cli_utils import configure_utf8_stdio, read_int

MIN_FACTOR = 1
MAX_FACTOR = 10


def build_multiplication_table(number: int, limit: int = MAX_FACTOR) -> list[str]:
    """Формирует строки таблицы умножения для числа от 1 до 10 с помощью цикла."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Число должно быть целым.")
    if number < MIN_FACTOR or number > MAX_FACTOR:
        raise ValueError(f"Число должно находиться в диапазоне от {MIN_FACTOR} до {MAX_FACTOR}.")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError("Верхняя граница таблицы должна быть целым положительным числом.")

    lines: list[str] = []
    for factor in range(1, limit + 1):
        lines.append(f"{number} × {factor} = {number * factor}")
    return lines


def run(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> list[str]:
    """Запрашивает число от 1 до 10, выводит таблицу умножения и возвращает её строки."""
    number = read_int(
        f"Введите число от {MIN_FACTOR} до {MAX_FACTOR}: ",
        min_value=MIN_FACTOR,
        max_value=MAX_FACTOR,
        input_fn=input_fn,
        output_fn=output_fn,
    )
    table_lines = build_multiplication_table(number)
    for line in table_lines:
        output_fn(line)
    return table_lines


def main() -> None:
    """Точка входа для Задания 3."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
