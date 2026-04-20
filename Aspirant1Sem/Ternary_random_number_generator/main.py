# main.py
# Основной скрипт для запуска моделирования, анализа и тестирования

import argparse
import numpy as np
import matplotlib.pyplot as plt
from ternary_gate import F1, F2
from transition_matrix import build_transition_matrix, stationary_distribution, compute_convergence_rate, compute_delta
from simulator import TRNGSimulator
from randomness_tests import chi_square_uniform, chi_square_independence, autocorrelation, runs_test
from collections import defaultdict
from state_manager import article_index

def run_theoretical_analysis(N, gate_func=F1):
    """Вычисляет стационарное распределение через матрицу Q."""
    print(f"\n=== Теоретический анализ для N={N} ===")
    Q, states, _ = build_transition_matrix(N, gate_func)
    p = stationary_distribution(Q, N)
    print(f"Размерность пространства состояний: {len(states)}")
    V = compute_convergence_rate(Q, N)
    print(f"Параметр скорости сходимости V = {V:.4f} (чем меньше, тем быстрее сходимость)")
    # Сортировка состояний по индексу из статьи
    sorted_pairs = sorted(zip(states, p), key=lambda x: article_index(x[0]))
    sorted_states, sorted_p = zip(*sorted_pairs)
    print(f"Стационарное распределение (все {len(sorted_p)} состояний, в порядке Ind(S)):")
    max_display = 20 if len(sorted_p) > 20 else len(sorted_p)
    for i in range(max_display):
        print(f"  {sorted_states[i]}: {sorted_p[i]:.6f}")
    if len(sorted_p) > max_display:
        print(f"  ... и ещё {len(sorted_p)-max_display} состояний")
    # Проверим равномерность выходов первого вентиля
    probs = defaultdict(float)
    for s, prob in zip(states, p):
        probs[s[0]] += prob
    print("Распределение выходов первого вентиля:")
    for val in (-1,0,1):
        print(f"  {val}: {probs[val]:.4f}")
    plt.figure(figsize=(10, 4))
    plt.bar(range(len(sorted_p)), sorted_p, width=0.8)
    plt.xlabel('Индекс состояния (порядок Ind(S))')
    plt.ylabel('Вероятность')
    plt.title(f'Стационарное распределение для N={N}')
    plt.grid(True, axis='y')
    plt.savefig(f'stationary_N{N}.png', dpi=150)
    plt.show()
    return p, states

def run_simulation(N, num_samples, delay_distr, gate_func, clock_D, output_gate, delay_params=None):
    print(f"\n=== Моделирование: N={N}, распределение={delay_distr}, выборок={num_samples} ===")
    if delay_params is None:
        delay_params = {}
    sim = TRNGSimulator(N=N, gate_func=gate_func, delay_distribution=delay_distr,
                        delay_params=delay_params, clock_D=clock_D,
                        record_output=output_gate)
    seq = sim.run(num_samples)
    return seq

def run_tests(seq, name="Последовательность"):
    """Проводит все статистические тесты."""
    print(f"\n--- Тесты для {name} ---")
    # 1. Равномерность
    stat, p = chi_square_uniform(seq)
    print(f"Хи-квадрат (равномерность): stat={stat:.4f}, p-value={p:.4f}")
    # 2. Биграммы
    stat2, p2 = chi_square_independence(seq, order=2)
    print(f"Хи-квадрат (независимость биграмм): stat={stat2:.4f}, p-value={p2:.4f}")
    # 3. Серии
    z, p_runs = runs_test(seq)
    print(f"Тест серий: Z = {z:.4f}, p-value = {p_runs:.4f}")
    # 4. Автокорреляция (первые 20 лагов)
    acf = autocorrelation(seq, max_lag=20)
    print("Автокорреляция (первые 5 лагов):", [f"{acf[l]:.4f}" for l in range(1,6)])
    return {"uniform_p": p, "bigram_p": p2, "acf": acf}

def plot_autocorrelation(acf, title="Автокорреляционная функция"):
    plt.figure()
    # plt.stem(range(len(acf)), acf, basefmt=" ") # убрал, чтобы в 0-ой позиции не было 1.
    plt.stem(range(1, len(acf)), acf[1:], basefmt=" ")
    plt.xlabel("Лаг")
    plt.ylabel("Автокорреляция")
    plt.title(title)
    plt.grid(True)
    plt.savefig("autocorr.png")
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Троичный TRNG симулятор")
    parser.add_argument("--N", type=int, default=2, help="Число вентилей")
    parser.add_argument("--num_samples", type=int, default=100000, help="Длина последовательности")
    parser.add_argument("--delay_distr", type=str, default="exponential", 
                        choices=["exponential","uniform","gamma","deterministic"],
                        help="Распределение задержек")
    parser.add_argument("--gate", type=str, default="F1", choices=["F1","F2"])
    parser.add_argument("--clock_D", type=float, default=8.0, help="Тактовый интервал D")
    parser.add_argument("--output_gate", type=int, default=0, help="Номер выходного вентиля (0..N-1)")
    parser.add_argument("--theoretical", action="store_true", help="Выполнить теоретический анализ")
    parser.add_argument("--delta", action="store_true", help="Вычислить δ для разных D")
    parser.add_argument("--seed", type=int, default=None, help="Seed для воспроизводимости")
    args = parser.parse_args()

    if args.seed is not None:
        np.random.seed(args.seed)

    gate = F1 if args.gate == "F1" else F2

    if args.theoretical:
        run_theoretical_analysis(args.N, gate)
        return
    
    if args.delta:
        Q, states, _ = build_transition_matrix(args.N, gate)
        for D in [2,4,8,16]:
            d = compute_delta(Q, args.N, D)
            print(f"D={D:2d}, δ={d:.2e}")
        return

    # Параметры для распределений
    delay_params = {}
    if args.delay_distr == 'exponential':
        delay_params = {'scale': 1.0}
    elif args.delay_distr == 'uniform':
        delay_params = {'low': 0.0, 'high': 2.0}
    elif args.delay_distr == 'gamma':
        delay_params = {'shape': 2.0, 'scale': 0.5}
    elif args.delay_distr == 'deterministic':
        delay_params = {'value': 1.0, 'epsilon': 0.01}

    seq = run_simulation(N=args.N, num_samples=args.num_samples,
                         delay_distr=args.delay_distr, gate_func=gate,
                         clock_D=args.clock_D, output_gate=args.output_gate,
                         delay_params=delay_params)
    results = run_tests(seq, f"N={args.N}, distr={args.delay_distr}")
    plot_autocorrelation(results["acf"], f"ACF для N={args.N}, {args.delay_distr}")

if __name__ == "__main__":
    main()