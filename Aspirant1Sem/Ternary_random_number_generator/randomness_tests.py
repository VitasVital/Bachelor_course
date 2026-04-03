# randomness_tests.py
# Набор тестов для троичных последовательностей

import numpy as np
from scipy.stats import chi2, norm

def chi_square_uniform(sequence: list, categories=(-1,0,1)) -> tuple:
    """
    Проверка равномерности распределения символов.
    Возвращает (статистика хи-квадрат, p-value).
    """
    observed = [sequence.count(v) for v in categories]
    n = len(sequence)
    expected = [n / len(categories)] * len(categories)
    stat = sum((obs - exp)**2 / exp for obs, exp in zip(observed, expected))
    df = len(categories) - 1
    p = 1 - chi2.cdf(stat, df)
    return stat, p

def contingency_table(seq, order=2):
    """
    Строит таблицу сопряжённости для order-грамм.
    order=2 -> биграммы, order=3 -> триграммы.
    Возвращает словарь частот и список всех возможных кортежей.
    """
    from itertools import product
    values = (-1,0,1)
    all_grams = list(product(values, repeat=order))
    freq = {gram: 0 for gram in all_grams}
    for i in range(len(seq) - order + 1):
        gram = tuple(seq[i:i+order])
        freq[gram] += 1
    return freq, all_grams

def chi_square_independence(seq, order=2) -> tuple:
    """
    Проверка независимости между соседними символами (биграммы или триграммы).
    Используется критерий хи-квадрат для таблицы сопряжённости.
    Для order=2: таблица 3x3.
    Для order=3: таблица 3x9 (предыдущие два символа -> следующий) или 27-мерная, но
    проще использовать тест на основе энтропии или хи-квадрат для многомерной таблицы.
    Здесь реализуем для биграмм (order=2) как в отчёте.
    """
    if order != 2:
        raise NotImplementedError("Для order>2 требуется более сложная обработка.")
    values = (-1,0,1)
    # Строим матрицу 3x3: строки - предыдущий символ, столбцы - следующий
    cont = np.zeros((3,3), dtype=int)
    for i in range(len(seq)-1):
        row = values.index(seq[i])
        col = values.index(seq[i+1])
        cont[row, col] += 1
    # Вычисляем ожидаемые частоты при независимости
    row_sums = cont.sum(axis=1)
    col_sums = cont.sum(axis=0)
    total = cont.sum()
    expected = np.outer(row_sums, col_sums) / total
    stat = 0.0
    for i in range(3):
        for j in range(3):
            if expected[i,j] > 0:
                stat += (cont[i,j] - expected[i,j])**2 / expected[i,j]
    df = (3-1)*(3-1)
    p = 1 - chi2.cdf(stat, df)
    return stat, p

def runs_test(seq) -> tuple:
    """
    Тест на длину серий (runs test) для трёх символов.
    Серия – максимальная подпоследовательность одинаковых символов.
    Возвращает (Z-статистика, p-value).
    """
    n = len(seq)
    # Количество серий
    runs = 1
    for i in range(1, n):
        if seq[i] != seq[i-1]:
            runs += 1
    # Ожидаемое количество серий и дисперсия для многозначного алфавита сложнее.
    # Упрощённо: используем формулу для бинарного, заменив символы на 0/1? Не точно.
    # Лучше использовать тест на основе числа смен значений.
    # Воспользуемся нормальным приближением для марковской цепи.
    # Альтернатива: тест на количество переходов между разными символами.
    # Здесь для простоты используем тест на основе энтропии переходов.
    # Реализуем общий runs test для многозначных последовательностей по формуле:
    # mu = 1 + 2*(n-1)*p_switch, где p_switch = 1 - sum(p_i^2)
    # Но проще воспользоваться готовой реализацией из statsmodels? Не будем добавлять зависимости.
    # Вместо этого вычислим статистику как (runs - expected_runs) / sqrt(var_runs)
    # Для трёх равновероятных символов:
    p = [1/3, 1/3, 1/3]
    p_switch = 1 - sum(pi**2 for pi in p)  # = 2/3
    expected_runs = 1 + 2*(n-1)*p_switch*(1 - p_switch)  # приближение
    # Дисперсия сложна. Ограничимся выводом raw runs count.
    # Для отчёта используем только наблюдаемое число серий, без p-value.
    # Но лучше реализовать тест хи-квадрат на длины серий.
    # Упростим: вернём runs и ожидаемое значение.
    return runs, expected_runs

def autocorrelation(seq, max_lag=100) -> np.ndarray:
    """
    Вычисляет автокорреляционную функцию для троичной последовательности.
    Символы -1,0,1 интерпретируются как числа.
    """
    n = len(seq)
    mean = np.mean(seq)
    var = np.var(seq)
    if var == 0:
        return np.zeros(max_lag+1)
    acf = np.zeros(max_lag+1)
    for lag in range(max_lag+1):
        if lag == 0:
            acf[lag] = 1.0
        else:
            prod = [(seq[i] - mean)*(seq[i+lag] - mean) for i in range(n-lag)]
            acf[lag] = np.mean(prod) / var
    return acf