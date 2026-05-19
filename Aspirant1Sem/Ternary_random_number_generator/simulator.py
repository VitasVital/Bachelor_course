# simulator.py
# Дискретно-событийное моделирование TRNG с поддержкой разных топологий

import numpy as np
from typing import List, Tuple, Callable, Optional
from ternary_gate import F1
from state_manager import generate_all_states, exclude_homogeneous_states

class TRNGSimulator:
    """
    Базовый симулятор троичного генератора на основе джиттера.
    Поддерживает разные топологии: 'ring' (кольцо), 'ring_omit_output' (кольцо с пропущенным выходом),
    'parallel_single' (параллельные независимые N=1).
    """
    def __init__(self, N: int, gate_func=F1, delay_distribution='exponential',
                 delay_params=None, clock_D: float = 8.0, record_output: int = 0,
                 topology: str = 'ring'):
        """
        :param topology: 'ring' - кольцо (стандарт), 'ring_omit_output' - кольцо, но record_output игнорируется,
                         'parallel_single' - N параллельных N=1 генераторов (record_output выбирает один из них).
        """
        self.N = N
        self.gate_func = gate_func
        self.delay_distribution = delay_distribution
        self.delay_params = delay_params if delay_params else {}
        self.clock_D = clock_D
        self.record_output = record_output
        self.topology = topology
        
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
            scale = params.get('scale', 1.0)
            return np.random.exponential(scale)
        elif dist == 'uniform':
            low = params.get('low', 0.0)
            high = params.get('high', 2.0)
            return np.random.uniform(low, high)
        elif dist == 'gamma':
            shape = params.get('shape', 2.0)
            scale = params.get('scale', 0.5)
            return np.random.gamma(shape, scale)
        elif dist == 'deterministic':
            return params.get('value', 1.0)
        else:
            raise ValueError(f"Неизвестное распределение: {dist}")

    def _next_state_ring(self, state, k):
        """Переключение в кольцевой топологии"""
        a = state[k]
        b = state[(k-1) % self.N]
        new_out = self.gate_func(a, b)
        if new_out == state[k]:
            return None
        new_state_list = list(state)
        new_state_list[k] = new_out
        new_state = tuple(new_state_list)
        return new_state

    def run(self, num_steps: int) -> List[int]:
        if self.topology == 'parallel_single':
            single = TRNGSimulator(N=1, gate_func=self.gate_func,
                           delay_distribution=self.delay_distribution,
                           delay_params=self.delay_params,
                           clock_D=self.clock_D, record_output=0, topology='ring')
            return single.run(num_steps)

        sequence = []
        current_time = 0.0
        last_sample_time = 0.0
        # Инициализируем таймеры (уже есть в __init__, но нужно сохранить)
        # Основной цикл по событиям
        while len(sequence) < num_steps:
            k = np.argmin(self.timers)
            dt = self.timers[k]
            # Проверяем, допустим ли переход, не продвигая время
            state = self.idx_to_state[self.current_state_idx]

            if self.topology == 'ring':
                new_state = self._next_state_ring(state, k)
            elif self.topology == 'ring_omit_output':
                new_state = self._next_state_ring(state, k)  # динамика та же
            else:
                raise ValueError(f"Неизвестная топология {self.topology}")

            if new_state is not None and new_state in self.state_to_idx:
                current_time += dt
                self.timers -= dt
                self.current_state_idx = self.state_to_idx[new_state]
                self.timers[k] = self._generate_delay()
            else:
                # Переход невозможен (состояние запрещено или выход не меняется)
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
                out_val = state_current[out_idx]
                sequence.append(out_val)
                last_sample_time += self.clock_D
        return sequence