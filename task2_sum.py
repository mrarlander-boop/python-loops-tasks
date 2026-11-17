"""Задание 2. Вычисление суммы чисел от 1 до N с помощью цикла."""

from __future__ import annotations

from collections.abc import Callable

from cli_utils import configure_utf8_stdio, read_int


def sum_to_n(n: int) -> tuple[int, list[int]]:
    """Вычисляет сумму всех целых чисел от 1 до N с помощью цикла for."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("N должно быть целым числом.")
    if n < 1:
        raise ValueError("N должно быть положительным целым числом (>= 1).")

    total = 0
    terms: list[int] = []
    for number in range(1, n + 1):
        total += number
        terms.append(number)
    return total, terms


def format_sum_result(n: int) -> str:
    """Возвращает отформатированную строку с выражением суммы и результатом."""
    total, terms = sum_to_n(n)
    expression = " + ".join(str(term) for term in terms)
    return f"Результат: {expression} = {total}"


def run(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> int:
    """Запрашивает N, выводит выражение суммы от 1 до N и возвращает сумму."""
    n = read_int(
        "Введите целое положительное число N: ",
        min_value=1,
        input_fn=input_fn,
        output_fn=output_fn,
    )
    total, _ = sum_to_n(n)
    output_fn(f"Введено: {n}")
    output_fn(format_sum_result(n))
    return total


def main() -> None:
    """Точка входа для Задания 2."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
