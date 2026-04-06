# transition_matrix.py
# Построение матрицы переходов Q и вычисление стационарного распределения

import numpy as np
from scipy.linalg import eig, lstsq
from typing import Tuple, List, Callable
from state_manager import generate_all_states, exclude_homogeneous_states, build_state_mapping

def build_transition_matrix(N: int, gate_func: Callable[[int, int], int]):
    """
    Строит матрицу Q (размер M' x M'), где M' = 3^N - 3.
    Q[i,j] = количество способов перейти из состояния j в состояние i зёа один шаг.
    Возвращает Q, список состояний (исключая однородные), и маппинг состояние->индекс.
    """
    all_states = generate_all_states(N)
    states = exclude_homogeneous_states(all_states)
    M = len(states)
    state_to_idx = build_state_mapping(states)

    Q = np.zeros((M, M), dtype=int)

    for j_idx, state in enumerate(states):
        # Пробуем переключить каждый из N вентилей
        for k in range(N):
            # Входы вентиля k: собственный выход state[k] и выход предыдущего вентиля (k-1 mod N)
            a = state[k]
            b = state[(k - 1) % N]
            new_out = gate_func(a, b)
            if new_out == state[k]:
                # По условию (2) из статьи это не должно происходить, но оставим проверку
                continue
            # Формируем новое состояние
            new_state_list = list(state)
            new_state_list[k] = new_out
            new_state = tuple(new_state_list)
            if new_state in state_to_idx:
                i_idx = state_to_idx[new_state]
                Q[i_idx, j_idx] += 1
            # Если new_state оказался однородным (исключён), то переход в него невозможен
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
    p, _, _, _ = lstsq(A_aug, b)
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
    V = np.max(eigvals_real[mask]) - N
    return V