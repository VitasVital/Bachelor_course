# simulator.py
# Дискретно-событийное моделирование TRNG с поддержкой разных топологий

import numpy as np
from typing import List
from ternary_gate import F1
from state_manager import generate_all_states, exclude_homogeneous_states
from topologies import get_connections


class TRNGSimulator:
    """
    Базовый симулятор троичного генератора на основе джиттера.

    Поддерживаемые топологии:
      'ring'              — кольцо (стандарт);
      'ring_omit_output'  — кольцо, сэмплируется соседний выход;
      'parallel_single'   — N=1 (делегирование);
      'design1'           — Design 1, обобщённый на любое N;
      'design2'           — Design 2, только N=3.
    """

    def __init__(self, N: int, gate_func=F1, delay_distribution='exponential',
                 delay_params=None, clock_D: float = 8.0, record_output: int = 0,
                 topology: str = 'ring'):
        self.N = N
        self.gate_func = gate_func
        self.delay_distribution = delay_distribution
        self.delay_params = delay_params if delay_params else {}
        self.clock_D = clock_D
        self.record_output = record_output
        self.topology = topology

        # Списки соединений для design1/design2; (None, None) для кольцевых.
        self.in1, self.in2 = get_connections(topology, N)

        all_states = generate_all_states(N)
        self.states = exclude_homogeneous_states(all_states) if N > 1 else all_states
        self.state_to_idx = {s: i for i, s in enumerate(self.states)}
        self.idx_to_state = {i: s for i, s in enumerate(self.states)}

        # Текущее состояние (индекс)
        self.current_state_idx = np.random.choice(len(self.states))
        # Таймеры для каждого вентиля (время до следующего переключения)
        self.timers = np.zeros(N)
        self._reset_timers()

    def _reset_timers(self):
        for i in range(self.N):
            if self.delay_distribution == 'deterministic':
                # Добавляем малый случайный сдвиг (0..epsilon) для начальной фазы
                epsilon = self.delay_params.get('epsilon', 0.01)
                base = self.delay_params.get('value', 1.0)
                self.timers[i] = base + np.random.uniform(0, epsilon)
            else:
                self.timers[i] = self._generate_delay()

    def _generate_delay(self) -> float:
        """Генерирует случайную задержку согласно заданному распределению."""
        dist = self.delay_distribution
        params = self.delay_params
        if dist == 'exponential':
            return np.random.exponential(params.get('scale', 1.0))
        elif dist == 'uniform':
            return np.random.uniform(params.get('low', 0.0),
                                     params.get('high', 2.0))
        elif dist == 'gamma':
            return np.random.gamma(params.get('shape', 2.0),
                                   params.get('scale', 0.5))
        elif dist == 'deterministic':
            return params.get('value', 1.0)
        else:
            raise ValueError(f"Неизвестное распределение: {dist}")

    def _next_state(self, state, k):
        """
        Обобщённый переход:
          - если in1/in2 заданы (design1/design2) — берём state[in1[k]], state[in2[k]];
          - иначе — стандартное кольцо: state[k], state[(k-1) % N].
        """
        if self.in1 is not None:
            a = state[self.in1[k]]
            b = state[self.in2[k]]
        else:
            a = state[k]
            b = state[(k - 1) % self.N]

        new_out = self.gate_func(a, b)
        if new_out == state[k]:
            return None
        new_state_list = list(state)
        new_state_list[k] = new_out
        return tuple(new_state_list)

    def run(self, num_steps: int) -> List[int]:
        if self.topology == 'parallel_single':
            single = TRNGSimulator(N=1, gate_func=self.gate_func,
                                   delay_distribution=self.delay_distribution,
                                   delay_params=self.delay_params,
                                   clock_D=self.clock_D,
                                   record_output=0, topology='ring')
            return single.run(num_steps)

        sequence = []
        current_time = 0.0
        last_sample_time = 0.0
        # Основной цикл дискретно-событийного моделирования:
        #   - выбираем вентиль с минимальным оставшимся временем (np.argmin по таймерам);
        #   - если переход допустим и не ведёт в запрещённое состояние,
        #     применяем его и сбрасываем таймер этого вентиля;
        #   - каждые clock_D единиц модельного времени снимаем значение
        #     выходного вентиля (state_current[out_idx]) в последовательность.
        # Таймеры инициализированы в __init__ (через _reset_timers) и здесь
        # только обновляются, повторная инициализация не нужна.
        while len(sequence) < num_steps:
            k = np.argmin(self.timers)
            dt = self.timers[k]
            # Проверяем, допустим ли переход, не продвигая время
            state = self.idx_to_state[self.current_state_idx]

            new_state = self._next_state(state, k)

            if new_state is not None and new_state in self.state_to_idx:
                current_time += dt
                self.timers -= dt
                self.current_state_idx = self.state_to_idx[new_state]
                self.timers[k] = self._generate_delay()
            else:
                # Переход в запрещённое (однородное) состояние. Это возможно,
                # если у элемента оба входа идут от него самого (например,
                # у S2 в Design 2). Физически элемент остаётся на месте —
                # в матрице Q это самопереход (см. build_transition_matrix).
                # Устойчивых состояний в схеме нет (условие F(a,b) ≠ a,b
                # выполняется), но целевое состояние выведено из пространства.
                current_time += dt
                self.timers -= dt
                self.timers[k] = self._generate_delay()
            # Сэмплирование по тактовому сигналу (добавляем все пропущенные отсчёты)
            while current_time - last_sample_time >= self.clock_D:
                state_current = self.idx_to_state[self.current_state_idx]
                if self.topology == 'ring_omit_output':
                    # Используем любой выход, кроме record_output, например, (record_output+1)%N
                    out_idx = (self.record_output + 1) % self.N
                else:
                    out_idx = self.record_output
                sequence.append(state_current[out_idx])
                last_sample_time += self.clock_D
        return sequence