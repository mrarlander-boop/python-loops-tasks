"""Единое меню для запуска всех пяти заданий по циклам в Python."""

from __future__ import annotations

from collections.abc import Callable

import task1_sequence
import task2_sum
import task3_multiplication_table
import task4_even_odd_stats
import task5_guess_number
from cli_utils import configure_utf8_stdio, read_int

TASKS: dict[int, tuple[str, Callable[[], object]]] = {
    1: ("Вывод последовательности от 1 до 20", task1_sequence.main),
    2: ("Сумма чисел от 1 до N", task2_sum.main),
    3: ("Таблица умножения для числа от 1 до 10", task3_multiplication_table.main),
    4: ("Подсчёт чётных, нечётных и суммы 10 чисел", task4_even_odd_stats.main),
    5: ("Игра «Угадай число» от 1 до 100", task5_guess_number.main),
}


def run_menu(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
    tasks: dict[int, tuple[str, Callable[[], object]]] | None = None,
) -> None:
    """Запускает интерактивное меню выбора заданий до выбора выхода (0)."""
    task_map = tasks if tasks is not None else TASKS

    while True:
        output_fn("\n=== Практические задания по циклам ===")
        for number, (title, _) in task_map.items():
            output_fn(f"{number}. {title}")
        output_fn("0. Выход")

        choice = read_int(
            f"Выберите номер задания (0-{max(task_map)}): ",
            min_value=0,
            max_value=max(task_map),
            input_fn=input_fn,
            output_fn=output_fn,
        )
        if choice == 0:
            output_fn("Выход из программы.")
            return
        if choice not in task_map:
            output_fn("Ошибка: такого задания нет в меню.")
            continue

        _, runner = task_map[choice]
        output_fn("")
        runner()


def main() -> None:
    """Точка входа единого меню."""
    configure_utf8_stdio()
    run_menu()


if __name__ == "__main__":
    main()
