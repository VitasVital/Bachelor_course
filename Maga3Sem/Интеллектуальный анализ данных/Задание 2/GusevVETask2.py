import numpy as np
from scipy.spatial.distance import sqeuclidean

class HierarchicalAgglomerativeClustering:
    def __init__(self, n_clusters=2, linkage='_min_distance'):
        self.n_clusters = n_clusters
        self.calculate_cdist = { '_min_distance' : self._min_distance, 
                               '_max_distance' : self._max_distance,
                               '_avg_distance' : self._avg_distance,
                               '_method1_distance' : self._method1_distance,
                               '_method2_distance' : self._method2_distance,
                               }[linkage]
        
    # метод односвязной кластеризации
    @staticmethod
    def _min_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.min(distances)
    
    # метод полносвязной кластеризации
    @staticmethod
    def _max_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.max(distances)
    
    # метод среднего расстояния
    @staticmethod
    def _avg_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.average(distances)
    
    # Метод 1. Полусумма минимального и максимального расстояния между объектами из двух кластеров 
    @staticmethod
    def _method1_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return (np.min(distances) + np.max(distances)) / 2
    
    # Метод 2. Медианное расстояние между всеми парами объектов из двух кластеров
    @staticmethod
    def _method2_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.median(distances)
    
    #метки с минимальным расстоянием, то есть ближайшие кластеры объединяются в новый следующим образом:
    #всем объектам одного кластера присваиваются метки другого, после чего все новые метки,
    #которые больше меток другого кластера, уменьшаются на 1, то есть их нумерация сдвигается влево
    #для устранения пропусков в последовательности;
    @staticmethod
    def _update_labels(labels, min_cdist_idxs):
        labels[labels == min_cdist_idxs[1]] = min_cdist_idxs[0]
        labels[labels > min_cdist_idxs[1]] -= 1

        return labels
    
    # функция предсказания
    def fit_predict(self, X):
        labels = np.arange(len(X))
        clusters = [[x] for x in X]
        step = 0

        while len(clusters) > self.n_clusters:
            min_cdist, min_cdist_idxs = np.inf, []  #равно бесконечности и пустому списку

            print("\nШаг ", step)
            print("Матрица Dn расстояний между кластерами")
            for i in range(len(clusters) - 1):
                for j in range(i + 1, len(clusters)):
                    cdist = self.calculate_cdist(clusters[i], clusters[j])

                    if cdist < min_cdist:
                        min_cdist = cdist
                        min_cdist_idxs = (i, j)

            labels = self._update_labels(labels, min_cdist_idxs)
            clusters[min_cdist_idxs[0]].extend(clusters.pop(min_cdist_idxs[1]))

            print("n = len(clusters) = ", len(clusters))
            print("Номера кластеров для точек: ", np.array(labels))
            print("Минимальное рассояние между кластерами равно ", min_cdist)
            print("И это расстояние между кластерами в D: ", min_cdist_idxs)
            step+=1

        return np.array(labels)

# создание массива наблюдений
points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
             [1, 5, 3, 6, 4, 5, 2, 5]]).T
print(points)
ac = HierarchicalAgglomerativeClustering(n_clusters=2, linkage='_method2_distance')
ac_pred_res = ac.fit_predict(points)
print('\nРезультат предсказания', ac_pred_res)
