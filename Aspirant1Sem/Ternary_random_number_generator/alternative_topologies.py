# alternative_topologies.py
# Реализация различных топологий TRNG и их статистический анализ

import numpy as np
from simulator import TRNGSimulator
from randomness_tests import (
    chi_square_uniform, chi_square_independence, runs_test, autocorrelation,
    entropy, mutual_information, runs_length_distribution
)
import matplotlib.pyplot as plt
from paths import OUTPUT_DIR, ensure_output_dir
ensure_output_dir()

def evaluate_topology(topology, N, num_samples, delay_distr, gate_func, clock_D, output_gate, delay_params=None):
    """Запускает симулятор для заданной топологии и возвращает статистику"""
    sim = TRNGSimulator(N=N, gate_func=gate_func, delay_distribution=delay_distr,
                        delay_params=delay_params, clock_D=clock_D,
                        record_output=output_gate, topology=topology)
    seq = sim.run(num_samples)
    stats = {}
    # Базовые тесты
    stats['uniform_p'] = chi_square_uniform(seq)[1]
    stats['bigram_p'] = chi_square_independence(seq)[1]
    stats['runs_p'] = runs_test(seq)[1]
    acf = autocorrelation(seq, max_lag=20)
    stats['acf1'] = acf[1]
    # Дополнительные
    stats['entropy'] = entropy(seq)
    stats['mutual_info_lag1'] = mutual_information(seq, lag=1)
    stats['mutual_info_lag2'] = mutual_information(seq, lag=2)
    stats['runs_len_p'] = runs_length_distribution(seq)[1]
    return stats, seq

def compare_topologies():
    """Сравнивает несколько топологий в одинаковых условиях"""
    params = {
        'N': 3,
        'num_samples': 50000,
        'delay_distr': 'exponential',
        'gate_func': None,  # будет подставлен F1
        'clock_D': 8,
        'output_gate': 0,
        'delay_params': {'scale': 1.0}
    }
    from ternary_gate import F1
    params['gate_func'] = F1

    topologies = ['ring', 'ring_omit_output', 'parallel_single']
    results = {}
    for topo in topologies:
        print(f"Тестирование топологии: {topo}")
        stats, seq = evaluate_topology(topo, **params)
        results[topo] = stats
        # Сохраним последовательность для дальнейшего анализа
        np.savetxt(OUTPUT_DIR / f"seq_{topo}.txt", seq, fmt='%d')
    # Вывод таблицы
    print("\n=== Сравнение топологий ===")
    print("Топология\tp_равн\tp_бигр\tp_серий\tACF(1)\tЭнтропия\tMI1\tMI2\tp_дл_серий")
    for topo, s in results.items():
        print(f"{topo}\t{s['uniform_p']:.3f}\t{s['bigram_p']:.3f}\t{s['runs_p']:.3f}\t"
              f"{s['acf1']:.4f}\t{s['entropy']:.3f}\t{s['mutual_info_lag1']:.3f}\t"
              f"{s['mutual_info_lag2']:.3f}\t{s['runs_len_p']:.3f}")
    return results

if __name__ == "__main__":
    compare_topologies()