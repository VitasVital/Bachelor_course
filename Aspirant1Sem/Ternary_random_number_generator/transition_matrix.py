# transition_matrix.py
# Построение матрицы переходов Q и вычисление стационарного распределения

import numpy as np
from scipy.linalg import expm
from typing import Callable
from state_manager import (generate_all_states, exclude_homogeneous_states,
                           build_state_mapping)


def build_transition_matrix(N: int, gate_func: Callable[[int, int], int],
                            in1=None, in2=None):
    """
    Строит матрицу Q (размер M' x M', где M' = 3^N - 3 при N > 1).

    Если in1/in2 не заданы — используется кольцевая топология:
    in1[k] = k, in2[k] = (k-1) mod N.
    """
    if in1 is None or in2 is None:
        in1 = list(range(N))
        in2 = [(k - 1) % N for k in range(N)]

    all_states = generate_all_states(N)
    states = all_states if N == 1 else exclude_homogeneous_states(all_states)
    M = len(states)
    state_to_idx = build_state_mapping(states)

    Q = np.zeros((M, M), dtype=int)

    for j_idx, state in enumerate(states):
        # Пробуем переключить каждый из N вентилей
        for k in range(N):
            # Входы вентиля k: собственный выход state[k] и выход предыдущего вентиля (k-1 mod N)
            a = state[in1[k]]
            b = state[in2[k]]
            new_out = gate_func(a, b)
            if new_out == state[k]:
                # Элемент k не меняет выход — это тоже самопереход.
                Q[j_idx, j_idx] += 1
                continue
            new_state_list = list(state)
            new_state_list[k] = new_out
            new_state = tuple(new_state_list)
            if new_state in state_to_idx:
                Q[state_to_idx[new_state], j_idx] += 1
            else:
                # Целевое состояние однородное и исключено из пространства.
                # Физически элемент «пытается» переключиться, но запрещённое
                # состояние недостижимо → он остаётся на месте (самопереход).
                Q[j_idx, j_idx] += 1
    # Проверка: сумма элементов каждого столбца должна быть равна N
    col_sums = Q.sum(axis=0)
    if not np.allclose(col_sums, N):
        raise ValueError(f"Ошибка: суммы столбцов Q = {col_sums}, ожидается {N}")
    return Q, states, state_to_idx

def stationary_distribution(Q: np.ndarray, N: int) -> np.ndarray:
    """
    Вычисляет стационарное распределение вероятностей P_bar,
    решая систему Q * P = N * P, sum(P)=1.
    Используется метод наименьших квадратов.
    """
    M = Q.shape[0]
    A = Q - N * np.eye(M)
    # Добавляем строку для нормировки
    A_aug = np.vstack([A, np.ones(M)])
    b = np.zeros(M + 1)
    b[-1] = 1.0
    # Решаем переопределённую систему
    p, _, _, _ = np.linalg.lstsq(A_aug, b, rcond=None)
    p = np.maximum(p, 0)
    p = p / np.sum(p)
    return p

def compute_convergence_rate(Q: np.ndarray, N: int) -> float:
    """
    Вычисляет параметр V – скорость сходимости к стационарному распределению.
    V = max{ Re(λ) : λ – собственное значение Q, λ != N }
    """
    eigvals = np.linalg.eigvals(Q)
    # Отфильтровываем собственное значение, равное N (с учётом погрешности)
    eigvals_real = np.real(eigvals)
    # Находим максимальное значение, не равное N
    mask = np.abs(eigvals - N) > 1e-6
    if not np.any(mask):
        return -np.inf
    return np.max(eigvals_real[mask]) - N


def compute_delta(Q: np.ndarray, N: int, D: float) -> float:
    """
    Вычисляет расстояние δ между стационарной матрицей и exp(D * Matr).
    δ = max_{u,v} |P_bar[u] - Astab(D)[u,v]|
    """
    M = Q.shape[0]
    Matr = Q - N * np.eye(M)
    Astab = expm(D * Matr)
    # Стационарное распределение (нормированный собственный вектор Q с собственным числом N)
    p = stationary_distribution(Q, N)
    # Стационарная матрица: каждый столбец = p
    Stab = np.tile(p, (M, 1)).T  # размер M x M, столбцы одинаковые
    return np.max(np.abs(Stab - Astab))