# randomness_tests.py
# Расширенный набор тестов для троичных последовательностей + NIST

import numpy as np
from scipy.stats import chi2, norm, chi2_contingency, chisquare
from collections import Counter
import math

# -------------------------- Базовые тесты (троичные) --------------------------
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

# -------------------------- Дополнительные троичные метрики --------------------------
def entropy(seq, base=2):
    """Энтропия Шеннона в битах на символ (base=2) или нат (base=e)"""
    freq = Counter(seq)
    probs = [f/len(seq) for f in freq.values()]
    ent = -sum(p * math.log(p) / math.log(base) for p in probs)
    return ent

def mutual_information(seq, lag=1):
    """Взаимная информация I(X_t; X_{t+lag}) в битах"""
    n = len(seq) - lag
    joint_counts = Counter()
    for i in range(n):
        joint_counts[(seq[i], seq[i+lag])] += 1
    p_xy = {k: v/n for k,v in joint_counts.items()}
    p_x = Counter(seq[:n])
    p_y = Counter(seq[lag:])
    p_x = {k: v/n for k,v in p_x.items()}
    p_y = {k: v/n for k,v in p_y.items()}
    mi = 0.0
    for (x,y), pxy in p_xy.items():
        if pxy > 0:
            mi += pxy * math.log2(pxy / (p_x[x] * p_y[y]))
    return mi

def runs_length_distribution(seq, max_len=10):
    """
    Распределение длин серий одинаковых символов.
    Возвращает χ²-статистику и p-value (сравнение с теоретическим распределением).
    """
    # Собираем все длины серий
    lengths = []
    current_len = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            current_len += 1
        else:
            lengths.append(current_len)
            current_len = 1
    lengths.append(current_len)

    # Наблюдаемые частоты (с группировкой хвоста)
    observed = [0] * max_len
    for l in lengths:
        if l >= max_len:
            observed[-1] += 1
        else:
            observed[l-1] += 1

    # Теоретические вероятности для равновероятных символов (длина серии l):
    # p(l) = (2/3) * (1/3)^(l-1) для l >= 1
    theo_probs = []
    for l in range(1, max_len):
        theo_probs.append((2/3) * (1/3)**(l-1))
    # Хвост: вероятность длины >= max_len
    theo_probs.append((1/3)**(max_len-1))

    expected = [p * len(lengths) for p in theo_probs]
    # χ² тест
    stat = 0.0
    for o, e in zip(observed, expected):
        if e > 0:
            stat += (o - e)**2 / e
    df = max_len - 1
    p = 1 - chi2.cdf(stat, df)
    return stat, p

# -------------------------- NIST тесты (через библиотеку nistrng) --------------------------
def run_nist_tests(seq_trits, bit_encoding=None, shuffle_bits=True):
    """
    Преобразует троичную последовательность в битовую с возможным перемешиванием битов.
    """
    if bit_encoding is None:
        bit_encoding = {-1: '00', 0: '01', 1: '10'}

    # Шаг 1: кодирование в биты
    pairs = [bit_encoding[t] for t in seq_trits]
    
    if shuffle_bits:
        # Шаг 2: разделяем на первые и вторые биты
        first_bits = [int(p[0]) for p in pairs]
        second_bits = [int(p[1]) for p in pairs]
        # Перемешиваем: сначала все первые, затем все вторые
        bits = first_bits + second_bits
    else:
        bits = [int(b) for pair in pairs for b in pair]

    # Далее стандартный код с nistrng
    from nistrng import pack_sequence, check_eligibility_all_battery, run_all_battery, SP800_22R1A_BATTERY
    binary_seq = pack_sequence(bits)
    eligible = check_eligibility_all_battery(binary_seq, SP800_22R1A_BATTERY)
    results = run_all_battery(binary_seq, eligible, False)
    report = {}
    for res, _ in results:
        report[res.name] = {'p_value': res.score, 'passed': res.passed}
    return report

def block_entropy_test(seq, block_size=3):
    """
    Тест «Покер»: равномерность распределения блоков длины block_size.
    Возвращает χ²-статистику и p-value.
    """
    from collections import Counter
    from scipy.stats import chi2
    blocks = [tuple(seq[i:i+block_size]) for i in range(0, len(seq)-block_size+1, block_size)]
    if not blocks:
        return 0, 1.0
    observed = Counter(blocks)
    expected_count = len(blocks) / (3**block_size)
    stat = sum((count - expected_count)**2 / expected_count for count in observed.values())
    df = 3**block_size - 1
    p = 1 - chi2.cdf(stat, df)
    return stat, p

def gap_test(seq, symbol=0, max_gap=20):
    """
    Gap-тест для заданного символа. Проверяет распределение расстояний между появлениями symbol.
    """
    from scipy.stats import chi2
    positions = [i for i, s in enumerate(seq) if s == symbol]
    gaps = [positions[i+1] - positions[i] - 1 for i in range(len(positions)-1)]
    if not gaps:
        return 0, 1.0
    # Теоретическое распределение геометрическое: P(gap = g) = (2/3)^g * (1/3)
    observed = [0]*(max_gap+1)
    for g in gaps:
        if g >= max_gap:
            observed[-1] += 1
        else:
            observed[g] += 1
    expected = [len(gaps) * ( (2/3)**g * (1/3) ) for g in range(max_gap)]
    expected.append(len(gaps) * ( (2/3)**max_gap ))  # хвост
    # Убираем нулевые ожидания
    stat = 0
    for o,e in zip(observed, expected):
        if e > 0:
            stat += (o-e)**2 / e
    df = max_gap  # число степеней свободы упрощённо
    p = 1 - chi2.cdf(stat, df)
    return stat, p

def linear_complexity_over_gf3(seq):
    """
    Вычисляет линейную сложность (минимальную длину LFSR) над GF(3)
    для троичной последовательности с символами -1, 0, 1.
    Реализация алгоритма Берлекампа-Месси.
    Возвращает длину LFSR (L).
    """
    # Отображение -1 -> 2 (GF(3)), 0 -> 0, 1 -> 1
    gf3 = {-1: 2, 0: 0, 1: 1}
    a = [gf3[x] for x in seq]
    n = len(a)
    # Инициализация
    C = [1]          # текущий полином связи
    B = [1]          # предыдущий полином связи
    L = 0            # текущая длина LFSR
    m = 1            # сдвиг
    b = 1            # предыдущая невязка
    for i in range(n):
        # Вычисление невязки d
        d = 0
        for j in range(L + 1):
            if j < len(C):
                d = (d + C[j] * a[i - j]) % 3
        if d == 0:
            m += 1
        else:
            T = C[:]
            # inv(b) в GF(3): 1 -> 1, 2 -> 2, потому что 2*2=4≡1 mod 3
            inv_b = 1 if b == 1 else (2 if b == 2 else 0)
            factor = (d * inv_b) % 3
            # Расширяем C до нужной длины
            while len(C) < len(B) + m:
                C.append(0)
            for j in range(len(B)):
                C[j + m] = (C[j + m] - factor * B[j]) % 3
            # Удаляем ведущие нули
            while len(C) > 0 and C[-1] == 0:
                C.pop()
            if 2 * L <= i:
                L = i + 1 - L
                B = T[:]
                b = d
                m = 1
            else:
                m += 1
    return L