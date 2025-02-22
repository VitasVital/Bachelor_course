import numpy as np
from scipy.spatial.distance import sqeuclidean
import copy

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

    @staticmethod
    def ClearClusters(self):
        for i in range(len(self.clusters)):
            for j in range(i, len(self.clusters)):
                self.clusters[i][j] = 0

    
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
    def _min_distance(self):
        distance_i = 1
        distance_j = 0
        for i in range(1, len(self.clusters) - 1):
            for j in range(0, i):
                if self.clusters[i, j] < self.clusters[distance_i, distance_j]:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j]
        for i in range(0, len(self.clusters)):
            distance_i_i = self.clusters[distance_i][i] if self.clusters[distance_i][i] != 0 else self.clusters[i][distance_i]
            distance_j_j = self.clusters[distance_j][i] if self.clusters[distance_j][i] != 0 else self.clusters[i][distance_j]
            self.clusters[distance_i, i] = min(distance_i_i, distance_j_j)
            self.clusters[distance_j, i] = min(distance_i_i, distance_j_j)
            self.clusters[i, distance_i] = min(distance_i_i, distance_j_j)
            self.clusters[i, distance_j] = min(distance_i_i, distance_j_j)
        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.clusters = np.delete(self.clusters, (distance_j), axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, (distance_j), axis=1) # удаление колонки
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Минимальное рассояние между кластерами равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)
        
    
    # метод полносвязной кластеризации
    @staticmethod
    def _max_distance(self):
        distance_i = 1
        distance_j = 0
        for i in range(1, len(self.clusters) - 1):
            for j in range(0, i):
                if self.clusters[i, j] < self.clusters[distance_i, distance_j]:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j]
        for i in range(0, len(self.clusters)):
            distance_i_i = self.clusters[distance_i][i] if self.clusters[distance_i][i] != 0 else self.clusters[i][distance_i]
            distance_j_j = self.clusters[distance_j][i] if self.clusters[distance_j][i] != 0 else self.clusters[i][distance_j]
            self.clusters[distance_i, i] = max(distance_i_i, distance_j_j)
            self.clusters[distance_j, i] = max(distance_i_i, distance_j_j)
            self.clusters[i, distance_i] = max(distance_i_i, distance_j_j)
            self.clusters[i, distance_j] = max(distance_i_i, distance_j_j)
        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.clusters = np.delete(self.clusters, (distance_j), axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, (distance_j), axis=1) # удаление колонки
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Максимальное рассояние между кластерами равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)
    
    # метод среднего расстояния
    @staticmethod
    def _avg_distance(self):
        distance_i = 1
        distance_j = 0
        for i in range(1, len(self.clusters) - 1):
            for j in range(0, i):
                if self.clusters[i, j] < self.clusters[distance_i, distance_j]:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j]
        for i in range(0, len(self.clusters)):
            distance_i_i = self.clusters[distance_i][i] if self.clusters[distance_i][i] != 0 else self.clusters[i][distance_i]
            distance_j_j = self.clusters[distance_j][i] if self.clusters[distance_j][i] != 0 else self.clusters[i][distance_j]
            clusters_points_i_len = len(self.clusters_points[distance_i])
            clusters_points_j_len = len(self.clusters_points[distance_j])
            self.clusters[distance_i, i] = (distance_i_i * clusters_points_i_len + distance_j_j * clusters_points_j_len) / (clusters_points_i_len + clusters_points_j_len)
            self.clusters[distance_j, i] = (distance_i_i * clusters_points_i_len + distance_j_j * clusters_points_j_len) / (clusters_points_i_len + clusters_points_j_len)
            self.clusters[i, distance_i] = (distance_i_i * clusters_points_i_len + distance_j_j * clusters_points_j_len) / (clusters_points_i_len + clusters_points_j_len)
            self.clusters[i, distance_j] = (distance_i_i * clusters_points_i_len + distance_j_j * clusters_points_j_len) / (clusters_points_i_len + clusters_points_j_len)
        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.clusters = np.delete(self.clusters, (distance_j), axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, (distance_j), axis=1) # удаление колонки
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Среднее рассояние между кластерами равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)
    
    # Метод 1. Полусумма минимального и максимального расстояния между объектами из двух кластеров 
    @staticmethod
    def _method1_distance(self):
        distance_i = 1
        distance_j = 0
        for i in range(1, len(self.clusters) - 1):
            for j in range(0, i):
                if self.clusters[i, j] < self.clusters[distance_i, distance_j]:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j]
        for i in range(0, len(self.clusters)):
            distance_i_i = self.clusters[distance_i][i] if self.clusters[distance_i][i] != 0 else self.clusters[i][distance_i]
            distance_j_j = self.clusters[distance_j][i] if self.clusters[distance_j][i] != 0 else self.clusters[i][distance_j]
            self.clusters[distance_i, i] = (max(distance_i_i, distance_j_j) + min(distance_i_i, distance_j_j)) / 2
            self.clusters[distance_j, i] = (max(distance_i_i, distance_j_j) + min(distance_i_i, distance_j_j)) / 2
            self.clusters[i, distance_i] = (max(distance_i_i, distance_j_j) + min(distance_i_i, distance_j_j)) / 2
            self.clusters[i, distance_j] = (max(distance_i_i, distance_j_j) + min(distance_i_i, distance_j_j)) / 2
        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.clusters = np.delete(self.clusters, (distance_j), axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, (distance_j), axis=1) # удаление колонки
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Полусумма минимального и максимального расстояния между объектами из двух кластеров равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)
    
    # Метод 2. Медианное расстояние между всеми парами объектов из двух кластеров
    @staticmethod
    def _method2_distance(self):
        distance_i = 1
        distance_j = 0
        for i in range(1, len(self.clusters) - 1):
            for j in range(0, i):
                if self.clusters[i, j] < self.clusters[distance_i, distance_j]:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j]
        point_nums = []
        for point in self.clusters_points[distance_i]:
            point_nums.append(point[0])
        for point in self.clusters_points[distance_j]:
            point_nums.append(point[0])
        point_nums.sort()
        for i in range(0, len(self.clusters)):
            distances_in_clusters = []
            for j in range(0, len(self.clusters_copy)):
                for point_num in point_nums:
                    distance_in_cluster = self.clusters_copy[point_num][j] if self.clusters_copy[point_num][j] != 0 else self.clusters_copy[j][point_num]
                    distances_in_clusters.append(distance_in_cluster)
            self.clusters[distance_i, i] = np.median(distances_in_clusters)
            self.clusters[distance_j, i] = np.median(distances_in_clusters)
            self.clusters[i, distance_i] = np.median(distances_in_clusters)
            self.clusters[i, distance_j] = np.median(distances_in_clusters)


        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.clusters = np.delete(self.clusters, (distance_j), axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, (distance_j), axis=1) # удаление колонки
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Медианное расстояние между всеми парами объектов из двух кластеров равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)
    
    # функция предсказания
    def fit_predict(self, points):
        self.clusters = ManhattanDistance(points)
        self.clusters_copy = copy.copy(self.clusters)
        print('Манхэттенское расстояние\n', self.clusters)
        self.labels = np.arange(len(points))
        
        self.clusters_points = [point for point in points]
        self.clusters_points = [[[point, self.clusters_points[point]]] for point in range(len(points))]
        step = 0
        while len(self.clusters) > self.n_clusters:
            print("\nШаг ", step)
            self.calculate_cdist(self)
            step+=1

        return np.array(self.labels)

# создание массива наблюдений
points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
             [1, 5, 3, 6, 4, 5, 2, 5]]).T
print(points)
ac = HierarchicalAgglomerativeClustering(n_clusters=2, linkage='_method1_distance')
ac_pred_res = ac.fit_predict(points)
print('\nРезультат предсказания', ac_pred_res)
