import numpy as np
from scipy.spatial.distance import sqeuclidean

# функция вычисления Манхэттенского расстояния
def ManhattanDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.abs(input_points[j, 0] - input_points[i, 0]) + np.abs(input_points[j, 1] - input_points[i, 1])
    return result_function

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
        # assign a cluster number to labels
        labels[labels == min_cdist_idxs[1]] = min_cdist_idxs[0]
        labels[labels > min_cdist_idxs[1]] -= 1

        return labels
    
    # функция предсказания
    def fit_predict(self, points):
        clusters = ManhattanDistance(points)
        labels = np.arange(len(points))
        print('Манхэттенское расстояние\n', clusters)
        
        clusters_points = [[point] for point in points]
        step = 0
        while len(clusters) > self.n_clusters:
            print("\nШаг ", step)
            minDistance_i = 1
            minDistance_j = 0
            for i in range(1, len(clusters) - 1):
                for j in range(0, i):
                    if clusters[i, j] < clusters[minDistance_i, minDistance_j]:
                        minDistance_i = i
                        minDistance_j = j
            minDistance = clusters[minDistance_i, minDistance_j]
            for i in range(0, len(clusters)):
                minDistance_i_i = clusters[minDistance_i][i] if clusters[minDistance_i][i] != 0 else clusters[i][minDistance_i]
                minDistance_j_j = clusters[minDistance_j][i] if clusters[minDistance_j][i] != 0 else clusters[i][minDistance_j]
                clusters[minDistance_i, i] = min(minDistance_i_i, minDistance_j_j)
                clusters[minDistance_j, i] = min(minDistance_i_i, minDistance_j_j)
                clusters[i, minDistance_i] = min(minDistance_i_i, minDistance_j_j)
                clusters[i, minDistance_j] = min(minDistance_i_i, minDistance_j_j)
            clusters_points[minDistance_i].append(clusters_points[minDistance_j])
            clusters_points.pop(minDistance_j)
            clusters = np.delete(clusters, (minDistance_j), axis=0) # удаление строки
            clusters = np.delete(clusters, (minDistance_j), axis=1) # удаление колонки
            labels = self._update_labels(labels, (minDistance_i, minDistance_j))
            for clusters_point in clusters_points:
                print(clusters_point)

            print("n = len(clusters) = ", len(clusters))
            print("Номера кластеров для точек: ", np.array(labels))
            print("Минимальное рассояние между кластерами равно ", minDistance)
            print("И это расстояние между кластерами в D: ", (minDistance_i, minDistance_j))
            print('Матрица Db расстояний между кластерами', clusters)
            step+=1

        return np.array(labels)

# создание массива наблюдений
points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
             [1, 5, 3, 6, 4, 5, 2, 5]]).T
print(points)
ac = HierarchicalAgglomerativeClustering(n_clusters=2, linkage='_method2_distance')
ac_pred_res = ac.fit_predict(points)
print('\nРезультат предсказания', ac_pred_res)
