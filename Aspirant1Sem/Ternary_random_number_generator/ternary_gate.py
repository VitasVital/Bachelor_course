# ternary_gate.py
# Реализация троичных логических функций по статье Latypov, Stolov (2017)

from typing import Tuple

# Определим троичные значения как целые числа -1, 0, 1
TRIT_VALUES = (-1, 0, 1)

def F1(a: int, b: int) -> int:
    """
    Функция F1 из таблицы 1 статьи.
    F(0,0)=1, F(1,1)=-1, F(-1,-1)=0.
    Для всех остальных пар возвращает третий символ, отличный от a и b.
    """
    if a == 0 and b == 0:
        return 1
    if a == 1 and b == 1:
        return -1
    if a == -1 and b == -1:
        return 0
    # Для неравных аргументов или смешанных: возвращаем единственное значение, не равное a и b
    # Поскольку все три значения различны, работает всегда
    s = set(TRIT_VALUES)
    s.discard(a)
    s.discard(b)
    return s.pop()

def F2(a: int, b: int) -> int:
    """
    Функция F2 из таблицы 1 статьи.
    F(0,0)=1, F(1,1)=-1, F(-1,-1)=1.
    Для остальных пар – аналогично F1.
    """
    if a == 0 and b == 0:
        return 1
    if a == 1 and b == 1:
        return -1
    if a == -1 and b == -1:
        return 1
    s = set(TRIT_VALUES)
    s.discard(a)
    s.discard(b)
    return s.pop()
