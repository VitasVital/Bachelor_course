import numpy as np
import copy
import time
from pandas import read_csv, DataFrame, Series
from sklearn.linear_model import LogisticRegression

with open('titanic_data.txt') as f:
    text = [line for line in f]

titanic_data_array = []
for i in text:
    numb = ''
    numb_array = []
    for j in i:
        if j != ',' and j != '\n':
            numb += j
        else:
            numb_array.append(copy.copy(float(numb)))
            numb = ''
    titanic_data_array.append(numb_array)

y = []
x = []
for i in titanic_data_array:
    y.append(i[0])
    x.append(i[1:])

train_titanic_data_array = titanic_data_array[:int(len(titanic_data_array) * 0.8)]
test_titanic_data_array = titanic_data_array[int(len(titanic_data_array) * 0.8):len(titanic_data_array) - 1]


def LeftСlassifier(beta, xi, yi):
    res = (1 / (1 + np.exp(-beta.T @ xi))) ** yi
    return res

def RightСlassifier(beta, xi, yi):
    res = (1 - (1 / (1 + np.exp(-beta.T @ xi)))) ** (1 - yi)
    return res

def Сlassifier(arr, beta):
    l = 0
    for i in arr:
        yi = i[0]
        xi = np.array(i[1:])
        l += np.log(LeftСlassifier(beta, xi, yi) * RightСlassifier(beta, xi, yi))
    return l

def Gradient(arr, beta):
    l = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    for i in arr:
        yi = np.array(i[0])
        xi = np.array(i[1:])
        l += (yi - (1 / (1 + np.exp(-beta.T @ xi)))) * xi
    return l

def Gradient_descent(arr, beta, step):
    beta_t1 = beta + step * Gradient(arr, beta)
    return beta_t1

def Logistic_regression(beta, x):
    LeftСlassifier = 1 / (1 + np.exp(-beta.T @ x))
    RightСlassifier = 1 - (1 / (1 + np.exp(-beta.T @ x)))
    if LeftСlassifier > RightСlassifier:
        return 1.0
    else:
        return 0.0

beta = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
step = 0.000001

start_time = time.time()
gradient = 0

for i in range(100000):
    beta = Gradient_descent(train_titanic_data_array, beta, step)
    #gradient = Gradient(train_titanic_data_array, beta)
    if np.array_equal(beta, gradient):
        print(gradient)
        break

classifier = Сlassifier(train_titanic_data_array, beta)
print(beta)
print(classifier)
print(time.time() - start_time)

my_x = [3, 0, 20, 0, 0, 54.69]

my_Logistic_regression = Logistic_regression(beta, my_x)
# my_LeftСlassifier = 1 / (1 + np.exp(-beta.T @ my_x))
# my_RightСlassifier = 1 - (1 / (1 + np.exp(-beta.T @ my_x)))
# print(my_LeftСlassifier, ' ', my_RightСlassifier)
if my_Logistic_regression == 1.0:
    print('Выживу')
else:
    print('Не выживу')

count = 0
for i in test_titanic_data_array:
    x = np.array(i[1:])
    if i[0] == Logistic_regression(beta, x):
        count += 1

print(len(test_titanic_data_array), ' ', count)