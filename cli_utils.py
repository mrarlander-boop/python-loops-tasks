"""Общие вспомогательные функции для консольного ввода-вывода."""

from __future__ import annotations

import sys
from collections.abc import Callable


def configure_utf8_stdio() -> None:
    """Настраивает стандартные потоки ввода-вывода на кодировку UTF-8, если это поддерживается."""
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        encoding = getattr(stream, "encoding", "") or ""
        if callable(reconfigure) and encoding.lower() != "utf-8":
            reconfigure(encoding="utf-8")


def _format_range_error(min_value: int | None, max_value: int | None) -> str:
    """Возвращает сообщение об ошибке для числа вне допустимого диапазона."""
    if min_value is not None and max_value is not None:
        return f"Ошибка: введите целое число от {min_value} до {max_value}."
    if min_value is not None:
        return f"Ошибка: введите целое число не меньше {min_value}."
    return f"Ошибка: введите целое число не больше {max_value}."


def read_int(
    prompt: str,
    min_value: int | None = None,
    max_value: int | None = None,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> int:
    """Запрашивает у пользователя целое число с проверкой корректности и границ."""
    while True:
        raw = input_fn(prompt)
        try:
            value = int(raw.strip())
        except ValueError:
            output_fn("Ошибка: введите корректное целое число.")
            continue

        if (min_value is not None and value < min_value) or (
            max_value is not None and value > max_value
        ):
            output_fn(_format_range_error(min_value, max_value))
            continue

        return value
