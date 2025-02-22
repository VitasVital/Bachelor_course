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
        point_nums = []
        for point in self.clusters_points[distance_i]:
            point_nums.append(point[0])
        for point in self.clusters_points[distance_j]:
            point_nums.append(point[0])
        point_nums.sort()
        min_distances_in_clusters = []
        for j in range(0, len(self.clusters_copy)):
            distances_in_clusters = []
            for point_num in point_nums:
                distance_in_cluster = self.clusters_copy[point_num][j] if self.clusters_copy[point_num][j] != 0 else self.clusters_copy[j][point_num]
                distances_in_clusters.append(distance_in_cluster)
            min_distances_in_clusters.append(np.min(distances_in_clusters))

        self.clusters = copy.copy(self.clusters_copy)
        for i in range(0, len(self.clusters)):
            self.clusters[distance_i, i] = min_distances_in_clusters[i]
            self.clusters[i, distance_i] = min_distances_in_clusters[i]
        
        point_nums = [i for i in point_nums if i != distance_i]
        self.clusters = np.delete(self.clusters, point_nums, axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, point_nums, axis=1) # удаление колонки


        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Минимальное рассояние между кластерами равно равно ", distance)
        print("И это расстояние между кластерами в D: ", (distance_i, distance_j))
        print('Матрица Dn расстояний между кластерами\n', self.clusters)
        
    
    # метод полносвязной кластеризации
    @staticmethod
    def _max_distance(self):
        distance_i = 1
        distance_j = 0
        for i in range(1, len(self.clusters) - 1):
            for j in range(0, i):
                if self.clusters[i, j] > self.clusters[distance_i, distance_j]:
                    distance_i = i
                    distance_j = j
        distance = self.clusters[distance_i, distance_j]
        point_nums = []
        for point in self.clusters_points[distance_i]:
            point_nums.append(point[0])
        for point in self.clusters_points[distance_j]:
            point_nums.append(point[0])
        point_nums.sort()
        max_distances_in_clusters = []
        for j in range(0, len(self.clusters_copy)):
            distances_in_clusters = []
            for point_num in point_nums:
                distance_in_cluster = self.clusters_copy[point_num][j] if self.clusters_copy[point_num][j] != 0 else self.clusters_copy[j][point_num]
                distances_in_clusters.append(distance_in_cluster)
            max_distances_in_clusters.append(np.max(distances_in_clusters))

        self.clusters = copy.copy(self.clusters_copy)
        for i in range(0, len(self.clusters)):
            self.clusters[distance_i, i] = max_distances_in_clusters[i]
            self.clusters[i, distance_i] = max_distances_in_clusters[i]
        
        point_nums = [i for i in point_nums if i != distance_i]
        self.clusters = np.delete(self.clusters, point_nums, axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, point_nums, axis=1) # удаление колонки

        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
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
        point_nums = []
        for point in self.clusters_points[distance_i]:
            point_nums.append(point[0])
        for point in self.clusters_points[distance_j]:
            point_nums.append(point[0])
        point_nums.sort()
        min_distances_in_clusters = []
        for j in range(0, len(self.clusters_copy)):
            distances_in_clusters = []
            for point_num in point_nums:
                distance_in_cluster = self.clusters_copy[point_num][j] if self.clusters_copy[point_num][j] != 0 else self.clusters_copy[j][point_num]
                distances_in_clusters.append(distance_in_cluster)
            min_distances_in_clusters.append(np.average(distances_in_clusters))

        self.clusters = copy.copy(self.clusters_copy)
        for i in range(0, len(self.clusters)):
            self.clusters[distance_i, i] = min_distances_in_clusters[i]
            self.clusters[i, distance_i] = min_distances_in_clusters[i]
        
        point_nums = [i for i in point_nums if i != distance_i]
        self.clusters = np.delete(self.clusters, point_nums, axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, point_nums, axis=1) # удаление колонки

        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
        self.labels = self._update_labels(self.labels, (distance_i, distance_j))
        for clusters_point in self.clusters_points:
            print(clusters_point)

        self.ClearClusters(self)
        print("n = len(clusters) = ", len(self.clusters))
        print("Номера кластеров для точек: ", np.array(self.labels))
        print("Среднее рассояние между кластерами равно равно ", distance)
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
        point_nums = []
        for point in self.clusters_points[distance_i]:
            point_nums.append(point[0])
        for point in self.clusters_points[distance_j]:
            point_nums.append(point[0])
        point_nums.sort()
        min_distances_in_clusters = []
        for j in range(0, len(self.clusters_copy)):
            distances_in_clusters = []
            for point_num in point_nums:
                distance_in_cluster = self.clusters_copy[point_num][j] if self.clusters_copy[point_num][j] != 0 else self.clusters_copy[j][point_num]
                distances_in_clusters.append(distance_in_cluster)
            min_distances_in_clusters.append((np.max(distances_in_clusters) + np.min(distances_in_clusters)) / 2)

        self.clusters = copy.copy(self.clusters_copy)
        for i in range(0, len(self.clusters)):
            self.clusters[distance_i, i] = min_distances_in_clusters[i]
            self.clusters[i, distance_i] = min_distances_in_clusters[i]
        
        point_nums = [i for i in point_nums if i != distance_i]
        self.clusters = np.delete(self.clusters, point_nums, axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, point_nums, axis=1) # удаление колонки

        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
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
        min_distances_in_clusters = []
        for j in range(0, len(self.clusters_copy)):
            distances_in_clusters = []
            for point_num in point_nums:
                distance_in_cluster = self.clusters_copy[point_num][j] if self.clusters_copy[point_num][j] != 0 else self.clusters_copy[j][point_num]
                distances_in_clusters.append(distance_in_cluster)
            min_distances_in_clusters.append(np.median(distances_in_clusters))

        self.clusters = copy.copy(self.clusters_copy)
        for i in range(0, len(self.clusters)):
            self.clusters[distance_i, i] = min_distances_in_clusters[i]
            self.clusters[i, distance_i] = min_distances_in_clusters[i]
        
        print(point_nums)
        point_nums = [i for i in point_nums if i != distance_i]
        print(point_nums)
        self.clusters = np.delete(self.clusters, point_nums, axis=0) # удаление строки
        self.clusters = np.delete(self.clusters, point_nums, axis=1) # удаление колонки

        self.clusters_points[distance_i].extend(self.clusters_points[distance_j])
        self.clusters_points.pop(distance_j)
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
ac = HierarchicalAgglomerativeClustering(n_clusters=2, linkage='_max_distance')
ac_pred_res = ac.fit_predict(points)
print('\nРезультат предсказания', ac_pred_res)
