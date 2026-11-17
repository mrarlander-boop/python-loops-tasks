"""Задание 1. Вывод последовательности чисел от 1 до 20 с помощью цикла for."""

from __future__ import annotations

from collections.abc import Callable

from cli_utils import configure_utf8_stdio


def build_sequence(start: int = 1, end: int = 20) -> list[int]:
    """Формирует список целых чисел от start до end включительно с помощью цикла for."""
    if isinstance(start, bool) or isinstance(end, bool) or not (
        isinstance(start, int) and isinstance(end, int)
    ):
        raise TypeError("Границы последовательности должны быть целыми числами.")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного.")

    sequence: list[int] = []
    for number in range(start, end + 1):
        sequence.append(number)
    return sequence


def print_sequence(
    start: int = 1,
    end: int = 20,
    output_fn: Callable[[str], None] = print,
) -> list[int]:
    """Выводит числа от start до end с помощью цикла for и возвращает список выведенных чисел."""
    numbers = build_sequence(start, end)
    for number in numbers:
        output_fn(str(number))
    return numbers


def main() -> None:
    """Точка входа для Задания 1."""
    configure_utf8_stdio()
    print("Числа от 1 до 20:")
    print_sequence(1, 20)


if __name__ == "__main__":
    main()
