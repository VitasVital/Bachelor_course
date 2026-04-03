# simulator.py
# Дискретно-событийное моделирование TRNG с произвольными распределениями задержек

import numpy as np
from typing import List, Tuple, Callable, Optional
from ternary_gate import F1
from state_manager import generate_all_states, exclude_homogeneous_states, state_index

class TRNGSimulator:
    """
    Симулятор троичного генератора на основе джиттера.
    Поддерживает разные распределения задержек переключения вентилей.
    """
    def __init__(self, N: int, gate_func: Callable[[int, int], int] = F1,
                 delay_distribution: str = 'exponential', delay_params: dict = None):
        """
        :param N: число вентилей
        :param gate_func: логическая функция (F1 или F2)
        :param delay_distribution: тип распределения ('exponential', 'uniform', 'gamma', 'deterministic')
        :param delay_params: параметры распределения (например, {'scale': 1.0})
        """
        self.N = N
        self.gate_func = gate_func
        self.delay_distribution = delay_distribution
        self.delay_params = delay_params if delay_params else {}

        # Состояния и их индексы
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
        """Инициализирует таймеры случайными значениями в соответствии с распределением."""
        for i in range(self.N):
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

    def step(self) -> Tuple[int, Tuple[int, ...], float]:
        """
        Выполняет один шаг дискретно-событийного моделирования.
        Находит вентиль с минимальным таймером, переключает его, обновляет таймеры.
        Возвращает (индекс нового состояния, само состояние, прошедшее время).
        """
        # Находим вентиль с наименьшим временем
        k = np.argmin(self.timers)
        dt = self.timers[k]

        # Обновляем все таймеры
        self.timers -= dt

        # Переключаем вентиль k
        current_state = self.idx_to_state[self.current_state_idx]
        a = current_state[k]
        b = current_state[(k - 1) % self.N]
        new_out = self.gate_func(a, b)
        # Формируем новое состояние
        new_state_list = list(current_state)
        new_state_list[k] = new_out
        new_state = tuple(new_state_list)

        # Если новое состояние однородное и N>1, оно исключено из списка.
        # В реальном устройстве такие состояния недостижимы, но в симуляции они могут возникнуть.
        # Для корректности отобразим его в ближайшее достижимое? Согласно теории, переход в них невозможен.
        # На практике в симуляции при N>1 такие состояния не должны появляться, если начальное состояние достижимо.
        # Проверим:
        if new_state not in self.state_to_idx:
            # Это может случиться только при ошибке, но на всякий случай выбросим исключение
            raise RuntimeError(f"Достигнуто недопустимое однородное состояние: {new_state}")
        self.current_state_idx = self.state_to_idx[new_state]

        # Генерируем новую задержку для переключившегося вентиля
        self.timers[k] = self._generate_delay()

        return self.current_state_idx, new_state, dt

    def run(self, num_steps: int, record_output: Optional[int] = None) -> List[int]:
        """
        Запускает моделирование на num_steps шагов.
        Если record_output задан (номер вентиля), записывает последовательность его выходов.
        Возвращает список троичных символов (-1,0,1) для указанного вентиля.
        """
        if record_output is None:
            record_output = 0  # по умолчанию записываем выход первого вентиля
        sequence = []
        for _ in range(num_steps):
            idx, state, _ = self.step()
            sequence.append(state[record_output])
        return sequence