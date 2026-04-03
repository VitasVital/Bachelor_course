import numpy as np
import scipy.stats as st
from scipy.linalg import expm
import heapq
from collections import Counter
import itertools

# ========================
# 1. ЛОГИКА ТРОИЧНЫХ ВЕНТИЛЕЙ
# ========================
def F1(a, b):
    """Функция F1 из Таблицы 1 (Latypov & Stolov, 2017)"""
    if a == b:
        return {0: 1, 1: -1, -1: 0}[a]
    return -(a + b)  # Для a != b в сбалансированной троичной логике

def F2(a, b):
    """Функция F2 (альтернативный вариант)"""
    if a == b:
        return {0: 1, 1: -1, -1: 1}[a]
    return -(a + b)

# ========================
# 2. ПОСТРОЕНИЕ МАТРИЦЫ ЭРЛАНГА
# ========================
def build_transition_matrix(N, func=F1):
    """Строит матрицу Q и Matr = Q - N*I для кольцевой схемы"""
    states = list(itertools.product([-1, 0, 1], repeat=N))
    M = len(states)
    Q = np.zeros((M, M), dtype=int)
    
    def state_to_idx(s):
        return sum((v + 1) * (3**k) for k, v in enumerate(s))
    
    for idx, state in enumerate(states):
        for k in range(N):
            a = state[k]
            b = state[(k - 1) % N]
            new_val = func(a, b)
            if new_val != a:
                new_state = list(state)
                new_state[k] = new_val
                new_idx = state_to_idx(new_state)
                Q[new_idx, idx] += 1
                
    # Исключаем недостижимые состояния <x,x,...,x> (Proposition 2)
    bad_mask = np.array([len(set(s)) == 1 for s in states])
    Q = Q[~bad_mask][:, ~bad_mask]
    Matr = Q - N * np.eye(Q.shape[0])
    return Matr, Q, [state_to_idx(s) for s, mask in zip(states, bad_mask) if not mask]

# ========================
# 3. ДИСКРЕТНО-СОБЫТИЙНАЯ СИМУЛЯЦИЯ (DES)
# ========================
class TernaryTRNGSimulator:
    def __init__(self, N=3, func=F1, delay_dist='exp', delay_params=1.0, 
                 clock_D=4.0, num_samples=10000, topology='ring'):
        self.N = N
        self.func = func
        self.delay_dist = delay_dist
        self.delay_params = delay_params
        self.D = clock_D
        self.num_samples = num_samples
        self.topology = topology
        # Инициализация допустимым состоянием (избегаем <x,x,...,x>)
        init_state = [-1, 0, 1] * (N // 3) + [-1, 0, 1][:N % 3]
        self.state = np.array(init_state[:N], dtype=int)
        
    def sample_delay(self):
        p = self.delay_params if hasattr(self.delay_params, '__iter__') else (self.delay_params,)
        if self.delay_dist == 'exp':
            return np.random.exponential(p[0])
        elif self.delay_dist == 'uniform':
            return np.random.uniform(p[0], p[1] if len(p)>1 else p[0]+1.0)
        elif self.delay_dist == 'normal':
            return max(1e-3, np.random.normal(p[0], p[1] if len(p)>1 else 0.1))
        elif self.delay_dist == 'weibull':
            return np.random.weibull(p[0]) * (p[1] if len(p)>1 else 1.0)
            
    def run(self):
        event_queue = []
        current_time = 0.0
        
        for i in range(self.N):
            dt = self.sample_delay()
            heapq.heappush(event_queue, (current_time + dt, i))
            
        outputs = []
        last_clock = 0.0
        
        while len(outputs) < self.num_samples:
            if not event_queue:
                break
            t_event, gate_idx = heapq.heappop(event_queue)
            current_time = t_event
            
            a = self.state[gate_idx]
            b = self.state[(gate_idx - 1) % self.N]
            new_val = self.func(a, b)
            if new_val != a:
                self.state[gate_idx] = new_val
                dt = self.sample_delay()
                heapq.heappush(event_queue, (current_time + dt, gate_idx))
                
            if current_time - last_clock >= self.D:
                outputs.append(tuple(self.state))
                last_clock = current_time
                
        return np.array(outputs)

# ========================
# 4. ТЕСТЫ НА СЛУЧАЙНОСТЬ
# ========================
def run_randomness_tests(samples):
    flat = samples.flatten()
    N = len(flat)
    
    obs = Counter(flat)
    expected = N / 3
    chi2 = sum((obs.get(i, 0) - expected)**2 / expected for i in [-1, 0, 1])
    p_val = 1 - st.chi2.cdf(chi2, 2)
    
    bigrams = list(zip(flat[:-1], flat[1:]))
    bg_obs = Counter(bigrams)
    bg_expected = N / 9
    chi2_bg = sum((bg_obs.get(pair, 0) - bg_expected)**2 / bg_expected for pair in itertools.product([-1,0,1], repeat=2))
    p_bg = 1 - st.chi2.cdf(chi2_bg, 8)
    
    corr = np.corrcoef(flat[:-1], flat[1:])[0, 1]
    
    probs = np.array([obs.get(v, 0)/N for v in [-1, 0, 1]])
    entropy = -np.sum(probs * np.log2(probs + 1e-9))
    
    return {
        'chi2_uni': f"{chi2:.3f} (p={p_val:.4f})",
        'chi2_bigram': f"{chi2_bg:.3f} (p={p_bg:.4f})",
        'autocorrelation_lag1': f"{corr:.4f}",
        'entropy_bits': f"{entropy:.3f} (макс={np.log2(3):.3f})"
    }

# ========================
# ЗАПУСК
# ========================
if __name__ == "__main__":
    print("=== Генератор на основе работ Р.Х. Латыпова и Е.Л. Столова ===")
    
    Matr, Q, valid_idx = build_transition_matrix(N=3, func=F1)
    eig_vals, _ = np.linalg.eig(Q)
    eig_real = np.real(eig_vals)
    dominant = np.max(eig_real)
    # Безопасный расчёт V (второе по величине собственное число)
    secondary = eig_real[eig_real < dominant - 1e-9]
    V = np.max(secondary) if len(secondary) > 0 else dominant - 1
    print(f"N=3, Доминирующее λ={dominant:.2f}, V={V:.3f} (чем меньше V<0, тем быстрее сходимость)")
    
    # Исправлен delay_params: теперь это скаляр или кортеж (1.0,)
    sim = TernaryTRNGSimulator(N=3, func=F1, delay_dist='exp', delay_params=1.0, 
                               clock_D=4.0, num_samples=50000)
    samples = sim.run()
    
    results = run_randomness_tests(samples)
    print("\nРезультаты тестов:")
    for k, v in results.items():
        print(f"  {k}: {v}")