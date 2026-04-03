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

def state_index(state: Tuple[int, ...]) -> int:
    """
    Вычисляет индекс состояния по формуле (4) из статьи:
    Ind(S) = sum_{k=0}^{N-1} 3^k * (s_k + 1)
    """
    idx = 0
    for k, val in enumerate(state):
        idx += (val + 1) * (3 ** k)
    return idx

def index_to_state(idx: int, N: int) -> Tuple[int, ...]:
    """Обратное преобразование: по индексу и N восстанавливает состояние."""
    state = []
    for k in range(N):
        val = (idx // (3 ** k)) % 3 - 1  # потому что s_k+1 даёт 0,1,2
        state.append(val)
    return tuple(state)

def build_state_mapping(states: List[Tuple[int, ...]]) -> Dict[Tuple[int, ...], int]:
    """Создаёт словарь: состояние -> его порядковый номер (0..M-1)."""
    return {s: i for i, s in enumerate(states)}