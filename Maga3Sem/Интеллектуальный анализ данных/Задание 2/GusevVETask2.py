import numpy as np
from scipy.spatial.distance import sqeuclidean
import copy

# функция вычисления Манхэттенского расстояния
def ManhattanDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, len(input_points)):
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
        
    # метод односвязной кластеризации
    @staticmethod
    def _min_distance(self, distance_i, i):
        return np.min(self.clusters_list_distances[distance_i][i])
    
    # метод полносвязной кластеризации
    @staticmethod
    def _max_distance(self, distance_i, i):
        return np.max(self.clusters_list_distances[distance_i][i])
    
    # метод среднего расстояния
    @staticmethod
    def _avg_distance(self, distance_i, i):
        return np.average(self.clusters_list_distances[distance_i][i])
    
    # Метод 1. Полусумма минимального и максимального расстояния между объектами из двух кластеров 
    @staticmethod
    def _method1_distance(self, distance_i, i):
        return (np.max(self.clusters_list_distances[distance_i][i]) + np.min(self.clusters_list_distances[distance_i][i])) / 2
    
    # Метод 2. Медианное расстояние между всеми парами объектов из двух кластеров
    @staticmethod
    def _method2_distance(self, distance_i, i):
        return np.median(self.clusters_list_distances[distance_i][i])

    @staticmethod
    def _calculate_distance(self):
        distance_i = 0
        distance_j = 1
        for i in range(0, len(self.clusters)):
            for j in range(0, i):
                if i != j and self.clusters[i, j] < self.clusters[distance_i, distance_j] and self.clusters[i, j] != 0:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j] # поиск минимального растояния в матрице

        for i in range(0, len(self.clusters)):
            self.clusters_list_distances[distance_i][i].extend(self.clusters_list_distances[distance_j][i])
            self.clusters_list_distances[i][distance_i].extend(self.clusters_list_distances[distance_j][i]) # добавление новых дистаций в кластер
            calculated_distance = self.calculate_cdist(self, distance_i, i) # вычисление расстояния выбранным методом
            self.clusters[distance_i][i] = calculated_distance
            self.clusters[i][distance_i] = calculated_distance
        
        self.clusters = np.delete(self.clusters, distance_j, axis=0) # удаление строки кластеров
        self.clusters = np.delete(self.clusters, distance_j, axis=1) # удаление колонки кластеров
        for i in range(len(self.clusters_list_distances)):
            self.clusters_list_distances[i].pop(distance_j) # удаление строки координат добавленных кластеров
        self.clusters_list_distances.pop(distance_j) # удаление строки координат добавленных кластеров
        for i in range(len(self.clusters)):
            self.clusters[i, i] = 0

        self.clusters_points[distance_i].extend(self.clusters_points[distance_j]) # обхединение кластеров
        self.clusters_points.pop(distance_j)

        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Рассояние между кластерами равно равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)

    
    # функция предсказания
    def fit_predict(self, points):
        self.clusters = ManhattanDistance(points)
        self.clusters_copy = copy.copy(self.clusters)
        self.clusters_list_distances = []
        for i in range(len(self.clusters_copy)):
            empty_lists = [[] for _ in range(len(self.clusters_copy))]
            self.clusters_list_distances.append(empty_lists)
        for i in range(len(self.clusters_copy)):
            for j in range(len(self.clusters_copy)):
                self.clusters_list_distances[i][j].append(self.clusters_copy[i, j]) # создание матрицы, в которой дистанции находятся в списке

        print('Манхэттенское расстояние\n', self.clusters)
        self.labels = np.arange(len(points))
        
        self.clusters_points = [point for point in points]
        self.clusters_points = [[[point, self.clusters_points[point]]] for point in range(len(points))] # информация о координатах точек и их порядковый номер
        step = 0
        while len(self.clusters) > self.n_clusters:
            print("\nШаг ", step)
            self._calculate_distance(self)
            step+=1

        return np.array(self.labels)

# создание массива наблюдений
points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
             [1, 5, 3, 6, 4, 5, 2, 5]]).T
print(points)
ac = HierarchicalAgglomerativeClustering(n_clusters=2, linkage='_method2_distance')
ac_pred_res = ac.fit_predict(points)
print('\nРезультат предсказания', ac_pred_res)
# _min_distance
# _max_distance
# _avg_distance
# _method1_distance
# _method2_distance