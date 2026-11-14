# binary_trng.py
# Обобщенная реализация двоичных каскадных TRNG (GF(2)) из статьи Latypov 2019

import numpy as np
import argparse
from collections import Counter
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Вспомогательные функции для GF(2)
# ---------------------------------------------------------
def int_to_binary_array(val: int, n_bits: int) -> np.ndarray:
    """Преобразует целое число в бинарный массив длины n_bits (младший бит справа)."""
    return np.array([(val >> i) & 1 for i in range(n_bits)], dtype=int)

def binary_array_to_int(arr: np.ndarray) -> int:
    """Преобразует бинарный массив в целое число."""
    return sum((int(bit) << i) for i, bit in enumerate(arr))

def gf2_rank(matrix: np.ndarray) -> int:
    """Вычисляет ранг матрицы над полем GF(2)."""
    A = matrix.copy() % 2
    n_rows, n_cols = A.shape
    rank = 0
    for col in range(n_cols):
        pivot = -1
        for row in range(rank, n_rows):
            if A[row, col] == 1:
                pivot = row
                break
        if pivot != -1:
            # Меняем строки местами
            A[[rank, pivot]] = A[[pivot, rank]]
            # Обнуляем остальные элементы в столбце
            for row in range(n_rows):
                if row != rank and A[row, col] == 1:
                    A[row] = (A[row] + A[rank]) % 2
            rank += 1
    return rank

# ---------------------------------------------------------
# 2. Основной класс генератора
# ---------------------------------------------------------
class BinaryTRNG:
    def __init__(self, Conn: np.ndarray, beta: list[int]):
        """
        Conn: матрица соединений размера N x (N+M)
        beta: вектор управляющих сигналов на свободных входах (длина M)
        """
        self.Conn = np.array(Conn, dtype=int)
        self.N, self.total_cols = self.Conn.shape
        self.M = self.total_cols - self.N
        self.beta = np.array(beta, dtype=int)
        
        if len(self.beta) != self.M:
            raise ValueError(f"Длина beta ({len(self.beta)}) не совпадает с M ({self.M})")
            
        self.K = 2**self.N
        self.Tr = None
        self.P_bar = None

    def check_stable_states(self) -> bool:
        """
        Условие (4) из статьи: проверка отсутствия устойчивых состояний.
        Возвращает True, если устойчивых состояний НЕТ.
        """
        Ident = np.eye(self.N, dtype=int)
        Conn_NN = self.Conn[:, :self.N]
        
        # Delta = Conn[:, N:] * beta^T (mod 2)
        Delta = (self.Conn[:, self.N:] @ self.beta) % 2
        Delta = Delta.reshape(-1, 1)
        
        left_mat = (Ident + Conn_NN) % 2
        right_mat = np.hstack((left_mat, Delta))
        
        rank_left = gf2_rank(left_mat)
        rank_right = gf2_rank(right_mat)
        
        # Нет устойчивых состояний, если rank(left) < rank(right)
        return rank_left < rank_right

    def build_transient_matrix(self):
        """Алгоритм 1: Построение матрицы переходов Tr."""
        self.Tr = np.zeros((self.K, self.K), dtype=int)
        for q in range(self.K):
            alpha = int_to_binary_array(q, self.N)
            gamma = np.concatenate([alpha, self.beta])
            
            for i in range(self.N):
                new_val = int(np.dot(self.Conn[i, :], gamma) % 2)
                alpha_new = alpha.copy()
                alpha_new[i] = new_val
                r = binary_array_to_int(alpha_new)
                self.Tr[r, q] += 1

    def compute_stationary_distribution(self):
        """Вычисляет стационарное распределение (собственный вектор для с.з. N)."""
        if self.Tr is None:
            self.build_transient_matrix()
            
        eigvals, eigvecs = np.linalg.eig(self.Tr)
        idx = np.argmin(np.abs(eigvals - self.N))
        vec = np.real(eigvecs[:, idx])
        vec = np.abs(vec)
        self.P_bar = vec / np.sum(vec)
        return self.P_bar

    def get_output_probabilities(self, output_gates: list[int]) -> np.ndarray:
        """
        Вычисляет вероятности для выходного вектора, снимаемого с указанных вентилей.
        output_gates: список индексов вентилей (например, [1, 2, 4, 5])
        """
        if self.P_bar is None:
            self.compute_stationary_distribution()
            
        n_out = len(output_gates)
        out_probs = np.zeros(2**n_out)
        
        for state_idx in range(self.K):
            alpha = int_to_binary_array(state_idx, self.N)
            out_bits = alpha[output_gates]
            out_val = binary_array_to_int(out_bits)
            out_probs[out_val] += self.P_bar[state_idx]
            
        return out_probs

    def simulate_sequence(self, num_samples: int, output_gates: list[int], 
                          clock_D: float = 8.0, delay_scale: float = 1.0) -> list[int]:
        """
        Дискретно-событийное моделирование с экспоненциальными задержками (джиттер).
        Возвращает последовательность целых чисел (индексы выходных векторов).
        """
        sequence = []
        current_time = 0.0
        last_sample_time = 0.0
        
        # Текущее состояние (индекс)
        current_state_idx = np.random.randint(0, self.K)
        
        # Таймеры для каждого вентиля
        timers = np.random.exponential(delay_scale, self.N)
        
        while len(sequence) < num_samples:
            k = np.argmin(timers)
            dt = timers[k]
            
            current_time += dt
            timers -= dt
            
            # Обновляем состояние
            alpha = int_to_binary_array(current_state_idx, self.N)
            gamma = np.concatenate([alpha, self.beta])
            new_val = int(np.dot(self.Conn[k, :], gamma) % 2)
            
            alpha[k] = new_val
            current_state_idx = binary_array_to_int(alpha)
            
            # Сбрасываем таймер переключившегося вентиля
            timers[k] = np.random.exponential(delay_scale)
            
            # Сэмплирование по тактовому сигналу
            while current_time - last_sample_time >= clock_D:
                alpha_snap = int_to_binary_array(current_state_idx, self.N)
                out_bits = alpha_snap[output_gates]
                sequence.append(binary_array_to_int(out_bits))
                last_sample_time += clock_D
                
        return sequence

# ---------------------------------------------------------
# 3. CLI Интерфейс
# ---------------------------------------------------------
def parse_matrix(conn_str: str) -> np.ndarray:
    """Парсит строку '1,0,1;0,1,0' в numpy массив."""
    try:
        rows = conn_str.split(';')
        return np.array([[int(x.strip()) for x in row.split(',')] for row in rows])
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Неверный формат матрицы: {e}")

def parse_beta(beta_str: str) -> list[int]:
    """Парсит строку '1,0' в список [1, 0]."""
    try:
        return [int(x.strip()) for x in beta_str.split(',')]
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Неверный формат beta: {e}")

def main():
    parser = argparse.ArgumentParser(description="Обобщенный бинарный TRNG (Latypov 2019)")
    parser.add_argument("--conn", type=parse_matrix, required=True, 
                        help="Матрица соединений (строка, например '1,0,0,1;0,1,1,0')")
    parser.add_argument("--beta", type=parse_beta, default=None, 
                        help="Управляющий сигнал (через запятую, например '1,0'). Не нужен, если используется --compare")
    parser.add_argument("--compare", type=str, default=None,
                        help="Сравнить два сигнала: 'b1:b2' (например, '1,0:0,1'). Строит график разности.")
    parser.add_argument("--outputs", type=str, default="", 
                        help="Индексы выходных вентилей (через запятую, например '1,2,4,5'). Если не указано, берутся все.")
    parser.add_argument("--simulate", action="store_true", help="Запустить имитационное моделирование")
    parser.add_argument("--num_samples", type=int, default=50000, help="Длина выборки для симуляции")
    parser.add_argument("--plot", action="store_true", help="Построить график распределения вероятностей (для одиночного режима)")
    
    args = parser.parse_args()
    
        # Режим сравнения двух сигналов
    if args.compare:
        try:
            beta1_str, beta2_str = args.compare.split(':')
            beta1 = parse_beta(beta1_str)
            beta2 = parse_beta(beta2_str)
        except Exception as e:
            print(f"Ошибка в --compare (ожидается 'b1:b2'): {e}")
            return
            
        trng1 = BinaryTRNG(args.conn, beta1)
        trng2 = BinaryTRNG(args.conn, beta2)
        
        print(f"=== Сравнение сигналов ===")
        print(f"Сигнал 1: {beta1}, Сигнал 2: {beta2}")
        print(f"Отсутствие устойчивых состояний: {trng1.check_stable_states()} и {trng2.check_stable_states()}")
        
        if args.outputs:
            output_gates = [int(x.strip()) for x in args.outputs.split(',')]
        else:
            output_gates = list(range(trng1.N))
            
        trng1.build_transient_matrix()
        trng1.compute_stationary_distribution()
        probs1 = trng1.get_output_probabilities(output_gates)
        
        trng2.build_transient_matrix()
        trng2.compute_stationary_distribution()
        probs2 = trng2.get_output_probabilities(output_gates)
        
        diff = probs1 - probs2
        
        # --- ЛИНЕЙНЫЙ ГРАФИК (как Рис. 8 и 9 в статье) ---
        plt.figure(figsize=(10, 4))
        plt.plot(range(len(diff)), diff, marker='o', linestyle='-', color='b', markersize=6)
        plt.title(f"Разность вероятностей: {beta1} - {beta2}")
        plt.xlabel("Состояние (индекс выходного вектора)")
        plt.ylabel("Разность вероятностей")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.xticks(range(len(diff)))   # все целые индексы на оси X
        plt.tight_layout()
        plt.show()
        
        # Вывод топ-5 различий
        abs_diff = np.abs(diff)
        top_indices = np.argsort(abs_diff)[::-1][:5]
        print(f"\nТоп-5 различий:")
        for idx in top_indices:
            print(f"  Вектор {idx:0{len(output_gates)}b}: diff={diff[idx]:+.6f} (p1={probs1[idx]:.6f}, p2={probs2[idx]:.6f})")
            
        if args.simulate:
            print(f"\nСимуляция для {beta1}...")
            seq1 = trng1.simulate_sequence(args.num_samples, output_gates)
            emp_probs1 = np.zeros(len(probs1))
            for k, v in Counter(seq1).items():
                emp_probs1[k] = v / args.num_samples
                
            print(f"Симуляция для {beta2}...")
            seq2 = trng2.simulate_sequence(args.num_samples, output_gates)
            emp_probs2 = np.zeros(len(probs2))
            for k, v in Counter(seq2).items():
                emp_probs2[k] = v / args.num_samples
                
            emp_diff = emp_probs1 - emp_probs2
            print("\nСравнение теоретической и эмпирической разности:")
            for idx in top_indices:
                print(f"  Вектор {idx:0{len(output_gates)}b}: теор={diff[idx]:+.6f}, эмпир={emp_diff[idx]:+.6f}")
        return

    # Одиночный режим (как было раньше)
    if args.beta is None:
        print("Ошибка: укажите --beta или используйте --compare")
        return
        
    try:
        trng = BinaryTRNG(args.conn, args.beta)
    except ValueError as e:
        print(f"Ошибка инициализации: {e}")
        return
        
    print(f"=== Анализ схемы ===")
    print(f"Размерность: N={trng.N}, M={trng.M}")
    
    is_unstable = trng.check_stable_states()
    print(f"Отсутствие устойчивых состояний: {is_unstable}")
    if not is_unstable:
        print("[Внимание] Схема имеет устойчивые состояния при данном beta. Генератор может 'зависнуть'.")
    
    # Определяем выходные вентили
    if args.outputs:
        output_gates = [int(x.strip()) for x in args.outputs.split(',')]
    else:
        output_gates = list(range(trng.N)) # По умолчанию берем все выходы
    
    print(f"Выходные вентили: {output_gates}")
    
    # Теоретический расчет
    trng.build_transient_matrix()
    trng.compute_stationary_distribution()
    out_probs = trng.get_output_probabilities(output_gates)
    
    print(f"Размер выходного пространства: {len(out_probs)}")
    print("Теоретические вероятности (первые 10):")
    for i, p in enumerate(out_probs[:10]):
        print(f"  Вектор {i:0{len(output_gates)}b}: {p:.6f}")
        
    # Построение графика
    if args.plot:
        plt.figure(figsize=(10, 4))
        plt.bar(range(len(out_probs)), out_probs, color='b', alpha=0.7)
        plt.title(f"Распределение вероятностей выходного вектора (N={trng.N}, M={trng.M})")
        plt.xlabel("Индекс выходного вектора")
        plt.ylabel("Вероятность")
        plt.grid(True, axis='y')
        plt.show()
        
    # Имитационное моделирование
    if args.simulate:
        print(f"\nЗапуск симуляции ({args.num_samples} отсчетов)...")
        seq = trng.simulate_sequence(args.num_samples, output_gates)
        counts = Counter(seq)
        
        print("Эмпирические частоты (топ-5):")
        for vec_idx, count in counts.most_common(5):
            emp_p = count / args.num_samples
            theo_p = out_probs[vec_idx]
            print(f"  Вектор {vec_idx:0{len(output_gates)}b}: частота={emp_p:.6f} (теор={theo_p:.6f})")

if __name__ == "__main__":
    main()