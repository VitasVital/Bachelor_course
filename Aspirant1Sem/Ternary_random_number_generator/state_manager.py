# state_manager.py
# Кодирование/декодирование состояний генератора

from itertools import product
from typing import List, Tuple, Dict
import numpy as np

TRIT_VALUES = (-1, 0, 1)

def generate_all_states(N: int) -> List[Tuple[int, ...]]:
    """Генерирует все 3^N состояний как кортежи длины N."""
    return list(product(TRIT_VALUES, repeat=N))

def is_homogeneous(state: Tuple[int, ...]) -> bool:
    """Проверяет, является ли состояние однородным (все элементы равны)."""
    return all(x == state[0] for x in state)

def exclude_homogeneous_states(states: List[Tuple[int, ...]]) -> List[Tuple[int, ...]]:
    """Исключает состояния вида (x,x,...,x) для x=-1,0,1."""
    return [s for s in states if not is_homogeneous(s)]

def build_state_mapping(states: List[Tuple[int, ...]]) -> Dict[Tuple[int, ...], int]:
    """Создаёт словарь: состояние -> его порядковый номер (0..M-1)."""
    return {s: i for i, s in enumerate(states)}

def article_index(state: Tuple[int, ...]) -> int:
    """
    Индекс состояния по формуле Ind(S) = Σ 3^k (s_k + 1)
    (см. формулу (4) в статьях).
    """
    return sum((3 ** k) * (s + 1) for k, s in enumerate(state))