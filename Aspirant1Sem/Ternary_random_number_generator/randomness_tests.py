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
    # Подсчёт числа серий (runs)
    runs = 1
    for i in range(1, n):
        if seq[i] != seq[i-1]:
            runs += 1
    # Ожидаемое число серий для многозначного алфавита
    # Для равновероятных символов: mu = 1 + (n-1)*(1 - sum(p_i^2))
    # p_i = 1/3, sum(p_i^2) = 1/3
    p_switch = 1 - 1/3  # вероятность смены символа
    mu = 1 + (n-1) * p_switch
    # Дисперсия для многозначного алфавита (формула Уолла-Вольфовица)
    # var = (n-1)*p_switch*(1-p_switch) + (1 - 3*p_switch*(1-p_switch))
    # Приближённая формула:
    var = (n-1) * p_switch * (1 - p_switch) + (1 - 3 * p_switch * (1 - p_switch))
    # Упрощённо: можно использовать var = (n-1)*p_switch*(1-p_switch) + 1
    # Но для точности возьмём из литературы:
    # Для трёх равновероятных символов p_switch = 2/3, тогда mu = 1 + (n-1)*2/3
    # var = (n-1)*2/3*1/3 + (1 - 3*2/3*1/3) = (n-1)*2/9 + (1 - 2/3) = 2(n-1)/9 + 1/3
    var = 2*(n-1)/9 + 1/3
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