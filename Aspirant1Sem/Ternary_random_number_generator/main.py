# main.py
# Основной скрипт для запуска моделирования, анализа и тестирования

import argparse
import numpy as np
import matplotlib.pyplot as plt
from ternary_gate import F1, F2
from transition_matrix import build_transition_matrix, stationary_distribution
from simulator import TRNGSimulator
from randomness_tests import chi_square_uniform, chi_square_independence, autocorrelation, runs_test

def run_theoretical_analysis(N, gate_func=F1):
    """Вычисляет стационарное распределение через матрицу Q."""
    print(f"\n=== Теоретический анализ для N={N} ===")
    Q, states, _ = build_transition_matrix(N, gate_func)
    p = stationary_distribution(Q, N)
    print(f"Размерность пространства состояний: {len(states)}")
    print("Стационарное распределение (первые 10):")
    for i in range(min(10, len(p))):
        print(f"  {states[i]}: {p[i]:.4f}")
    # Проверим равномерность выходов первого вентиля
    from collections import defaultdict
    probs = defaultdict(float)
    for s, prob in zip(states, p):
        probs[s[0]] += prob
    print("Распределение выходов первого вентиля:")
    for val in (-1,0,1):
        print(f"  {val}: {probs[val]:.4f}")
    return p, states

def run_simulation(N, num_samples, delay_distr, gate_func=F1, record_output=0):
    """Запускает дискретно-событийное моделирование."""
    print(f"\n=== Моделирование: N={N}, распределение={delay_distr}, выборок={num_samples} ===")
    sim = TRNGSimulator(N, gate_func, delay_distribution=delay_distr)
    seq = sim.run(num_samples, record_output=record_output)
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
    runs, exp_runs = runs_test(seq)
    print(f"Число серий: {runs}, ожидаемое (прибл.): {exp_runs:.2f}")
    # 4. Автокорреляция (первые 20 лагов)
    acf = autocorrelation(seq, max_lag=20)
    print("Автокорреляция (первые 5 лагов):", [f"{acf[l]:.4f}" for l in range(1,6)])
    return {"uniform_p": p, "bigram_p": p2, "acf": acf}

def plot_autocorrelation(acf, title="Автокорреляционная функция"):
    plt.figure()
    plt.stem(range(len(acf)), acf, basefmt=" ")
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
    parser.add_argument("--theoretical", action="store_true", help="Выполнить теоретический анализ")
    parser.add_argument("--output", type=int, default=0, help="Номер выходного вентиля (0..N-1)")
    args = parser.parse_args()

    gate = F1 if args.gate == "F1" else F2

    if args.theoretical:
        run_theoretical_analysis(args.N, gate)
    
    seq = run_simulation(args.N, args.num_samples, args.delay_distr, gate, args.output)
    results = run_tests(seq, f"N={args.N}, distr={args.delay_distr}")
    plot_autocorrelation(results["acf"], f"ACF для N={args.N}, {args.delay_distr}")

if __name__ == "__main__":
    main()