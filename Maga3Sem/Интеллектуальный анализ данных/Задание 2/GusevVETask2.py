import numpy as np
from scipy.spatial.distance import sqeuclidean
from sklearn.datasets import make_blobs

class HierarchicalAgglomerativeClustering:
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters

    @staticmethod
    def _min_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.min(distances)
    
    @staticmethod
    def _max_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.max(distances)
    
    @staticmethod
    def _avg_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.average(distances)
    
    @staticmethod
    def _method1_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return (np.min(distances) + np.max(distances)) / 2
    
    @staticmethod
    def _method2_distance(c1, c2):
        distances = []
        for i in c1:
            for j in c2:
                distances.append(sqeuclidean(i, j))
        print(distances)
        return np.median(distances)

#2) метки с минимальным расстоянием, то есть ближайшие кластеры объединяются в новый следующим образом:
#всем объектам одного кластера присваиваются метки другого, после чего все новые метки,
#которые больше меток другого кластера, уменьшаются на 1, то есть их нумерация сдвигается влево
#для устранения пропусков в последовательности;

    @staticmethod
    def _update_labels(labels, min_cdist_idxs):
        # assign a cluster number to labels
        labels[labels == min_cdist_idxs[1]] = min_cdist_idxs[0]
        labels[labels > min_cdist_idxs[1]] -= 1

        return labels

    def fit_predict(self, X):
        labels = np.arange(len(X))
        clusters = [[x] for x in X]

        while len(clusters) > self.n_clusters:
            min_cdist, min_cdist_idxs = np.inf, []  #равно бесконечности и пустому списку

            print("Матрица Dn расстояний между кластерами")
            for i in range(len(clusters) - 1):
                for j in range(i + 1, len(clusters)):
                    cdist = self._method2_distance(clusters[i], clusters[j])

                    if cdist < min_cdist:
                        min_cdist = cdist
                        min_cdist_idxs = (i, j)

            labels = self._update_labels(labels, min_cdist_idxs)
            clusters[min_cdist_idxs[0]].extend(clusters.pop(min_cdist_idxs[1]))   #pop Возвращает элемент [на указанной позиции], удаляя его из списка: list.pop([i]).
            #extend() добавляет новые элементы в конец списка, но, в отличие от append(), принимает в качестве параметров итерируемые объекты: списки, кортежи и строки.
            #При этом объединяемые списки могут содержать элементы любых типов: например, вы можете объединить строки с числами или числа с кортежами.

            print("n = len(clusters) = ", len(clusters))
            print("Номера кластеров для точек: ", np.array(labels))
            print("Минимальное рассояние между кластерами равно ", min_cdist)
            print("И это расстояние между кластерами в D: ", min_cdist_idxs)

        return np.array(labels)
    
X2, y2 = make_blobs(n_samples=75, n_features=2, centers=2, random_state=0)   #centers = n_clusters=3  n_samples=75 должно делиться нацело на n_clusters    - для ac

points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
             [1, 5, 3, 6, 4, 5, 2, 5]]).T
ac = HierarchicalAgglomerativeClustering(n_clusters=2)   #centers = n_clusters=3  n_samples=75 должно делиться нацело на n_clusters   - для  X2, y2
ac_pred_res = ac.fit_predict(points)
print('prediction', ac_pred_res, sep='\n')
