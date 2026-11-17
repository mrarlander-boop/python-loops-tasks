"""Задание 4. Подсчёт чётных, нечётных чисел и суммы из 10 введённых целых чисел."""

from __future__ import annotations

from collections.abc import Callable, Iterable

from cli_utils import configure_utf8_stdio, read_int

NUMBERS_COUNT = 10


def analyze_numbers(numbers: Iterable[int]) -> tuple[int, int, int]:
    """Определяет количество чётных, нечётных чисел и их общую сумму."""
    even_count = 0
    odd_count = 0
    total_sum = 0

    for number in numbers:
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("Все элементы последовательности должны быть целыми числами.")
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        total_sum += number

    return even_count, odd_count, total_sum


def read_numbers(
    count: int = NUMBERS_COUNT,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> list[int]:
    """Последовательно считывает заданное количество целых чисел с клавиатуры."""
    if isinstance(count, bool) or not isinstance(count, int) or count < 1:
        raise ValueError("Количество чисел должно быть положительным целым числом.")

    numbers: list[int] = []
    for index in range(1, count + 1):
        value = read_int(
            f"Введите целое число ({index} из {count}): ",
            input_fn=input_fn,
            output_fn=output_fn,
        )
        numbers.append(value)
    return numbers


def run(
    count: int = NUMBERS_COUNT,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> tuple[int, int, int]:
    """Запрашивает 10 чисел, выводит статистику и возвращает (чётные, нечётные, сумма)."""
    numbers = read_numbers(count=count, input_fn=input_fn, output_fn=output_fn)
    even_count, odd_count, total_sum = analyze_numbers(numbers)
    output_fn(f"Количество чётных чисел: {even_count}")
    output_fn(f"Количество нечётных чисел: {odd_count}")
    output_fn(f"Сумма всех введённых чисел: {total_sum}")
    return even_count, odd_count, total_sum


def main() -> None:
    """Точка входа для Задания 4."""
    configure_utf8_stdio()
    run()


if __name__ == "__main__":
    main()
