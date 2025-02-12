import numpy as np
import pandas as pd

excel_path = 'C:/Users/vitaly.gusev/Desktop/Универ/Bachelor_course/Maga3Sem/Интеллектуальный анализ данных/Задание 1/GusevVE_Task1.xlsx'

# функция вычисления Манхэттенского расстояния
def ManhattanDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.abs(input_points[j, 0] - input_points[i, 0]) + np.abs(input_points[j, 1] - input_points[i, 1])
    return result_function

# функция вычисления расстояния Хэмминга
def HamingDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.sign(input_points[j, 0] - input_points[i, 0]) + np.sign(input_points[j, 1] - input_points[i, 1])
    return result_function

# функция вычисления Евклидова расстояния
def EuclideanDistance(input_points):
    result_function = np.zeros((len(input_points), len(input_points)))
    for i in range(0, len(input_points)):
        for j in range(0, i):
            result_function[i, j] = np.sqrt((input_points[j, 0] - input_points[i, 0])**2 + (input_points[j, 1] - input_points[i, 1])**2)
    return result_function

# считывание массива наблюдений из excel
df_orders = pd.read_excel(excel_path, index_col=None, header=None)
points = np.array(df_orders)
print(np.array(points))

# points = np.array([[2, 2, 4, 4, 5, 5, 7, 7],
#              [1, 5, 3, 6, 4, 5, 2, 5]]).T

# вычисление Манхэттенского расстояния
manhattanDistance = ManhattanDistance(points)
# вычисление расстояния Хэмминга
hamingDistance = HamingDistance(points)
# вычисление Евклидова расстояния
euclideanDistance = EuclideanDistance(points)

# вывод результатов расстояний
print('Манхэттенское расстояние\n', manhattanDistance)
print('Расстояние Хэмминга\n', hamingDistance)
print('Евклидово расстояние\n', euclideanDistance)
