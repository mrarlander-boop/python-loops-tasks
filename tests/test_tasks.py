"""Модульные тесты для всех пяти заданий по циклам и вспомогательных утилит."""

from __future__ import annotations

import sys
import unittest
from collections.abc import Callable
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import cli_utils
import main as menu_main
import task1_sequence
import task2_sum
import task3_multiplication_table
import task4_even_odd_stats
import task5_guess_number


def make_io(
    inputs: list[str],
) -> tuple[Callable[[str], str], Callable[[str], None], list[str]]:
    """Создаёт функции ввода/вывода и список сообщений для детерминированного тестирования CLI."""
    iterator = iter(inputs)
    outputs: list[str] = []

    def fake_input(prompt: str) -> str:
        outputs.append(prompt)
        return next(iterator)

    def fake_output(message: str) -> None:
        outputs.append(message)

    return fake_input, fake_output, outputs


class TestCliUtils(unittest.TestCase):
    """Тесты функции read_int."""

    def test_valid_integer_with_whitespace(self) -> None:
        fake_input, fake_output, outputs = make_io(["  42  "])
        result = cli_utils.read_int("Число: ", input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(result, 42)
        self.assertEqual(outputs, ["Число: "])

    def test_retries_on_non_integer_and_out_of_bounds(self) -> None:
        fake_input, fake_output, outputs = make_io(["abc", "0", "11", "7"])
        result = cli_utils.read_int(
            "Число: ",
            min_value=1,
            max_value=10,
            input_fn=fake_input,
            output_fn=fake_output,
        )
        self.assertEqual(result, 7)
        self.assertIn("Ошибка: введите корректное целое число.", outputs)
        self.assertIn("Ошибка: введите целое число от 1 до 10.", outputs)


class TestTask1Sequence(unittest.TestCase):
    """Тесты Задания 1 (вывод чисел от 1 до 20)."""

    def test_build_sequence_default(self) -> None:
        self.assertEqual(task1_sequence.build_sequence(), list(range(1, 21)))

    def test_print_sequence_outputs_lines(self) -> None:
        outputs: list[str] = []
        result = task1_sequence.print_sequence(output_fn=outputs.append)
        self.assertEqual(result, list(range(1, 21)))
        self.assertEqual(outputs, [str(i) for i in range(1, 21)])

    def test_invalid_bounds_raise(self) -> None:
        with self.assertRaises(ValueError):
            task1_sequence.build_sequence(10, 5)
        with self.assertRaises(TypeError):
            task1_sequence.build_sequence(True, 5)


class TestTask2Sum(unittest.TestCase):
    """Тесты Задания 2 (сумма чисел от 1 до N)."""

    def test_sum_to_five_matches_example(self) -> None:
        total, terms = task2_sum.sum_to_n(5)
        self.assertEqual(total, 15)
        self.assertEqual(terms, [1, 2, 3, 4, 5])
        self.assertEqual(task2_sum.format_sum_result(5), "Результат: 1 + 2 + 3 + 4 + 5 = 15")

    def test_sum_to_one(self) -> None:
        self.assertEqual(task2_sum.sum_to_n(1), (1, [1]))
        self.assertEqual(task2_sum.format_sum_result(1), "Результат: 1 = 1")

    def test_invalid_n_raises(self) -> None:
        for bad_n in (0, -3):
            with self.assertRaises(ValueError):
                task2_sum.sum_to_n(bad_n)
        with self.assertRaises(TypeError):
            task2_sum.sum_to_n(True)

    def test_run_interactive_retries_invalid_and_prints_result(self) -> None:
        fake_input, fake_output, outputs = make_io(["-1", "abc", "5"])
        total = task2_sum.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(total, 15)
        self.assertIn("Введено: 5", outputs)
        self.assertIn("Результат: 1 + 2 + 3 + 4 + 5 = 15", outputs)


class TestTask3MultiplicationTable(unittest.TestCase):
    """Тесты Задания 3 (таблица умножения)."""

    def test_table_for_four_matches_example(self) -> None:
        expected = [f"4 × {i} = {4 * i}" for i in range(1, 11)]
        self.assertEqual(task3_multiplication_table.build_multiplication_table(4), expected)

    def test_boundary_values_and_invalid_inputs(self) -> None:
        self.assertEqual(len(task3_multiplication_table.build_multiplication_table(1)), 10)
        self.assertEqual(len(task3_multiplication_table.build_multiplication_table(10)), 10)
        for bad in (0, 11, -2):
            with self.assertRaises(ValueError):
                task3_multiplication_table.build_multiplication_table(bad)
        with self.assertRaises(TypeError):
            task3_multiplication_table.build_multiplication_table(False)

    def test_run_interactive(self) -> None:
        fake_input, fake_output, outputs = make_io(["15", "4"])
        lines = task3_multiplication_table.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(lines[0], "4 × 1 = 4")
        self.assertEqual(lines[-1], "4 × 10 = 40")
        self.assertIn("4 × 2 = 8", outputs)


class TestTask4EvenOddStats(unittest.TestCase):
    """Тесты Задания 4 (подсчёт чётных, нечётных и суммы 10 чисел)."""

    def test_analyze_mixed_numbers(self) -> None:
        even_count, odd_count, total_sum = task4_even_odd_stats.analyze_numbers(
            [0, -2, 3, 4, -5, 6, 7, 8, 9, 10]
        )
        self.assertEqual((even_count, odd_count, total_sum), (6, 4, 40))

    def test_analyze_rejects_bool(self) -> None:
        with self.assertRaises(TypeError):
            task4_even_odd_stats.analyze_numbers([1, True, 3])

    def test_run_reads_ten_numbers_with_validation(self) -> None:
        inputs = ["1", "bad", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        fake_input, fake_output, outputs = make_io(inputs)
        stats = task4_even_odd_stats.run(input_fn=fake_input, output_fn=fake_output)
        self.assertEqual(stats, (5, 5, 55))
        self.assertIn("Количество чётных чисел: 5", outputs)
        self.assertIn("Количество нечётных чисел: 5", outputs)
        self.assertIn("Сумма всех введённых чисел: 55", outputs)


class TestTask5GuessNumber(unittest.TestCase):
    """Тесты Задания 5 (игра «Угадай число»)."""

    def test_guess_on_first_attempt(self) -> None:
        fake_input, fake_output, outputs = make_io(["50"])
        attempts = task5_guess_number.play_guess_game(
            secret=50,
            input_fn=fake_input,
            output_fn=fake_output,
        )
        self.assertEqual(attempts, 1)
        self.assertIn("Вы угадали число 50! Количество попыток: 1", outputs)

    def test_hints_and_invalid_inputs_do_not_count_as_attempts(self) -> None:
        fake_input, fake_output, outputs = make_io(["abc", "101", "20", "80", "42"])
        attempts = task5_guess_number.play_guess_game(
            secret=42,
            input_fn=fake_input,
            output_fn=fake_output,
        )
        self.assertEqual(attempts, 3)
        self.assertIn("Загаданное число больше", outputs)
        self.assertIn("Загаданное число меньше", outputs)
        self.assertIn("Вы угадали число 42! Количество попыток: 3", outputs)

    def test_random_secret_within_bounds(self) -> None:
        fake_input, fake_output, _ = make_io(["73"])
        with patch("task5_guess_number.random.randint", return_value=73) as mock_rand:
            attempts = task5_guess_number.play_guess_game(
                input_fn=fake_input,
                output_fn=fake_output,
            )
        mock_rand.assert_called_once_with(1, 100)
        self.assertEqual(attempts, 1)


class TestMainMenu(unittest.TestCase):
    """Тесты единого меню запуска."""

    def test_menu_dispatches_task_and_exits(self) -> None:
        called: list[str] = []
        fake_tasks = {1: ("Тест", lambda: called.append("ran"))}
        fake_input, fake_output, outputs = make_io(["9", "1", "0"])
        menu_main.run_menu(input_fn=fake_input, output_fn=fake_output, tasks=fake_tasks)
        self.assertEqual(called, ["ran"])
        self.assertIn("Выход из программы.", outputs)


if __name__ == "__main__":
    unittest.main()
