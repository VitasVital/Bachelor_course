import numpy as np

def ManhattanDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.abs(input_points[j, 0] - input_points[i, 0]) + np.abs(input_points[j, 1] - input_points[i, 1])
    return result_function

def HamingDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.sign(input_points[j, 0] - input_points[i, 0]) + np.sign(input_points[j, 1] - input_points[i, 1])
    return result_function

def EuclideanDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.sqrt((input_points[j, 0] - input_points[i, 0])**2 + (input_points[j, 1] - input_points[i, 1])**2)
    return result_function

points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
             [1, 5, 3, 6, 4, 5, 2, 5]]).T

manhattanDistance = ManhattanDistance(points)
hamingDistance = HamingDistance(points)
euclideanDistance = EuclideanDistance(points)

# print(manhattanDistance)
print(hamingDistance)
# print(euclideanDistance)