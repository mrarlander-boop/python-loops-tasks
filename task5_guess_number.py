"""Задание 5. Консольная игра «Угадай число» от 1 до 100."""

from __future__ import annotations

import random
from collections.abc import Callable

from cli_utils import configure_utf8_stdio, read_int

MIN_SECRET = 1
MAX_SECRET = 100


def evaluate_guess(guess: int, secret: int) -> str | None:
    """Сравнивает догадку с загаданным числом и возвращает подсказку или None при угадывании."""
    if guess < secret:
        return "Загаданное число больше"
    if guess > secret:
        return "Загаданное число меньше"
    return None


def play_guess_game(
    secret: int | None = None,
    min_value: int = MIN_SECRET,
    max_value: int = MAX_SECRET,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> int:
    """Запускает игру «Угадай число» и возвращает количество затраченных попыток."""
    if min_value > max_value:
        raise ValueError("Минимальное значение не может быть больше максимального.")

    if secret is None:
        target = random.randint(min_value, max_value)
    else:
        if isinstance(secret, bool) or not isinstance(secret, int):
            raise TypeError("Загаданное число должно быть целым.")
        if secret < min_value or secret > max_value:
            raise ValueError(f"Загаданное число должно быть от {min_value} до {max_value}.")
        target = secret

    output_fn(f"Игра «Угадай число»: я загадал число от {min_value} до {max_value}.")
    attempts = 0

    while True:
        guess = read_int(
            "Введите ваш вариант: ",
            min_value=min_value,
            max_value=max_value,
            input_fn=input_fn,
            output_fn=output_fn,
        )
        attempts += 1

        hint = evaluate_guess(guess, target)
        if hint is not None:
            output_fn(hint)
            continue

        output_fn(f"Вы угадали число {target}! Количество попыток: {attempts}")
        return attempts


def main() -> None:
    """Точка входа для Задания 5."""
    configure_utf8_stdio()
    play_guess_game()


if __name__ == "__main__":
    main()
