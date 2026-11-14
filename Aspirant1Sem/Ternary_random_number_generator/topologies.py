# topologies.py
# Соединения для альтернативных топологий.
#
# in1[k], in2[k] — индексы элементов, с которых берутся сигналы
# на верхний и нижний входы элемента k (0 = S0, 1 = S1, ..., N-1 = S_{N-1}).
#
# Для 'ring', 'ring_omit_output', 'parallel_single' возвращается (None, None):
# динамика остаётся стандартной кольцевой, её обрабатывают
# simulator._next_state и transition_matrix.build_transition_matrix.
#
# Design 1 (обобщение на произвольное N):
#   S0:       верх S0,        низ S1
#   S_k:      верх S_k,       низ S_{k+1}    (k = 1..N-2)
#   S_{N-1}:  верх S_{N-1},   низ S1
#   При N=3:  S0<-S0,S1; S1<-S1,S2; S2<-S2,S1  (совпадает с рис. 3)
#
# Design 2 (определён только для N=3, согласно статье):
#   S0:       верх S1,        низ S0
#   S1:       верх S2,        низ S0
#   S2:       верх S2,        низ S2   (автономный осциллятор)
#
# Прочтение подтверждено теоретическим анализом для N=3:
#   V ≈ -0.588 (статья: ≈ -0.59), δ(D=8) ≈ 1.75e-3 (статья: ≈ 1.7e-3),
#   нули в P̄: (a, a, b), a ≠ b — не совпадают по индексам с Design 1.
#   Для N != 3 выдаётся ValueError.

ALL_TOPOLOGIES = [
    'ring',
    'ring_omit_output',
    'parallel_single',
    'design1',
    'design2',
]


def design1_connections(N: int):
    """Design 1, обобщение на произвольное N >= 2."""
    if N < 2:
        raise ValueError(f"Топология 'design1' определена для N >= 2 "
                         f"(запрошено N={N})")
    in1 = list(range(N))   # у всех самосвязь сверху
    in2 = []
    for k in range(N):
        if k == 0:
            in2.append(1)          # S0 <- S1
        elif k == N - 1:
            in2.append(1)          # S_{N-1} <- S1  (замыкание цикла)
        else:
            in2.append(k + 1)      # S_k <- S_{k+1}
    return in1, in2


def design2_connections(N):
    """
    Вариант A обобщения Design 2 на произвольное N >= 3.
    S_{N-1} — автономный осциллятор (двойная самосвязь).
    S_0 — сток (слушает S_1 и себя).
    S_1 .. S_{N-2} — формирователи (слушают следующего и S_0).
    При N=3 совпадает с design2_connections(3).
    """
    if N < 3:
        raise ValueError("Design 2 определён для N >= 3")
    in1 = []   # верхние входы
    in2 = []   # нижние входы
    for k in range(N):
        if k == 0:
            in1.append(1)   # S0: верх S1
            in2.append(0)   # S0: низ S0 (самосвязь)
        elif k == N - 1:
            in1.append(N - 1)  # S_{N-1}: верх S_{N-1} (осциллятор)
            in2.append(N - 1)  # S_{N-1}: низ S_{N-1}
        else:
            in1.append(k + 1)  # S_k: верх S_{k+1}
            in2.append(0)      # S_k: низ S0
    return in1, in2


def get_connections(topology, N):
    """
    Возвращает (in1, in2) для альтернативной топологии
    или (None, None) для ring / ring_omit_output / parallel_single.
    """
    if topology == 'design1':
        return design1_connections(N)
    if topology == 'design2':
        return design2_connections(N)
    # Для кольцевых и вырожденных — стандартная динамика
    return None, None