# randomness_tests.py
# Набор тестов для троичных последовательностей

import numpy as np
from scipy.stats import chi2, norm, chi2_contingency, chisquare

def chi_square_uniform(sequence, categories=(-1,0,1)):
    """
    Проверка равномерности распределения символов.
    Возвращает (статистика хи-квадрат, p-value).
    """
    observed = [sequence.count(v) for v in categories]
    stat, p = chisquare(observed)
    return stat, p

def chi_square_independence(seq, order=2) -> tuple:
    """
    Проверка независимости между соседними символами (биграммы).
    Использует scipy.stats.chi2_contingency для таблицы сопряжённости 3x3.
    """
    if order != 2:
        raise NotImplementedError("Для order>2 требуется более сложная обработка.")
    
    values = (-1, 0, 1)
    # Строим матрицу сопряжённости 3x3
    cont = np.zeros((3, 3), dtype=int)
    for i in range(len(seq) - 1):
        row = values.index(seq[i])
        col = values.index(seq[i+1])
        cont[row, col] += 1
    
    # Используем готовую функцию
    chi2, p, dof, expected = chi2_contingency(cont)
    return chi2, p

def runs_test(seq):
    """
    Тест на серии (runs) для троичной последовательности.
    Возвращает (Z-статистика, p-value).
    """
    n = len(seq)
    if n < 2:
        return 0.0, 1.0
    runs = 1
    for i in range(1, n):
        if seq[i] != seq[i-1]:
            runs += 1
    mu = 1 + 2 * (n - 1) / 3
    # Точная дисперсия для трёх равновероятных категорий (Wald-Wolfowitz)
    var = (2 * n + 1) / 9
    z = (runs - mu) / np.sqrt(var)
    p = 2 * (1 - norm.cdf(abs(z)))
    return z, p

def autocorrelation(seq, max_lag=100):
    """
    Вычисляет автокорреляционную функцию для троичной последовательности.
    Символы -1,0,1 интерпретируются как числа.
    """
    x = np.array(seq, dtype=float)
    x = x - np.mean(x)
    var = np.var(x)
    if var == 0:
        return np.zeros(max_lag+1)
    # Вычисляем автокорреляцию через корреляцию
    corr = np.correlate(x, x, mode='full') / (len(x) * var)
    # Берём только положительные лаги (lag 0 в центре)
    acf = corr[len(x)-1 : len(x)+max_lag]
    return acf  # acf[0] = 1.0