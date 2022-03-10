import numpy as np
from scipy.optimize import minimize
import random as rn
import itertools as it
import json

def get_all_K(N):
    k = []

    stuff = [i for i in range(1, N + 1)]  # все комбинации k
    for L in range(0, len(stuff) + 1):
        for subset in it.combinations(stuff, L):
            k.append(list(subset))
    return k

def get_all_K_json(N):
    list_k = get_all_K(N)
    for i in range(len(list_k)):
        str1 = ', '.join(str(e) for e in list_k[i])
        list_k[i] = str1

    list_to_dictionary = []

    for i in range(len(list_k)):
        data_set = {"id": i, "combinations": list_k[i], "value": 0}
        list_to_dictionary.append(data_set)

    json_object = list_to_dictionary
    return json_object

def get_all_v_K_json(N, V_k):
    list_k = get_all_K(N)
    for i in range(len(list_k)):
        str1 = ', '.join(str(e) for e in list_k[i])
        list_k[i] = str1

    list_to_dictionary = []

    for i in range(len(list_k)):
        data_set = {"id": i, "combinations": list_k[i], "value": V_k[i]}
        list_to_dictionary.append(data_set)

    json_object = list_to_dictionary
    return json_object

def get_all_random_v_K_json(N):
    list_k = get_all_K(N)
    for i in range(len(list_k)):
        str1 = ', '.join(str(e) for e in list_k[i])
        list_k[i] = str1

    list_v_k = str(0)

    # rand_value = 100
    # for i in range(1, len(list_k)):
    #     list_v_k += (' ' + str(rn.randrange(rand_value, rand_value + 100)))
    #     rand_value += 100

    rand_value = 100
    sum = 0
    for i in range(N):
        rand_number = rand_value + 100
        list_v_k += (' ' + str(rn.randrange(rand_value, rand_number)))
        sum += rand_number

    rand_value += sum
    for i in range(N + 1, len(list_k)):
        list_v_k += (' ' + str(rn.randrange(rand_value, rand_value + 100)))
        rand_value += 100

    return list_v_k

def start_function():
    N = 3

    k = get_all_K(N)

    print('k ', k)

    res_array = []

    for item in it.permutations(range(N), N): #все комбинации последовательностей формирования общей коалиции
        res_array.append([i + 1 for i in list(item)])

    print('Sheply ', res_array)

    # V_k = [rn.randrange(100, 600) for i in k] #случайные V(k)
    V_k = [0, 150, 180, 170, 360, 380, 380, 560] #случайные V(k)
    V_k[0] = 0

    print('V(k) ', V_k)

    res_row = []
    for row in res_array:
        row_add = [0 for i in range(N)] #инициализируем строку для вектора шепли
        row_add[row[0] - 1] = V_k[row[0]]
        last_element_v_k = V_k[row[0]]
        for i in range(1, len(row)):
            for j in range(len(k)):
                if sorted(row[:i + 1]) == sorted(k[j]):
                    index_row = row[:i + 1]
                    row_add[index_row[len(index_row) - 1] - 1] = V_k[j] - last_element_v_k
                    last_element_v_k = V_k[j]
        res_row.append(row_add)

    res_row = np.array(res_row)
    for i in res_row:
        print(i)

    sum_row = res_row.T @ np.ones(len(res_row))

    print(sum_row)
    print(sum_row / len(res_row))
    return sum_row


def additivnost(N, V_k):
    list_k = get_all_K(N)
    for i in range(N + 1, len(list_k)):
        sum = 0
        for e in list_k[i]:
            sum += int(V_k[e])
        if (sum > int(V_k[i])):
            return False
    return True

def find_Sheply(N, V_k):
    k = get_all_K(N)

    res_array = []

    for item in it.permutations(range(N), N): #все комбинации последовательностей формирования общей коалиции
        res_array.append([i + 1 for i in list(item)])

    res_row = []
    for row in res_array:
        row_add = [0 for i in range(N)] #инициализируем строку для вектора шепли
        row_add[row[0] - 1] = V_k[row[0]]
        last_element_v_k = V_k[row[0]]
        for i in range(1, len(row)):
            for j in range(len(k)):
                if sorted(row[:i + 1]) == sorted(k[j]):
                    index_row = row[:i + 1]
                    row_add[index_row[len(index_row) - 1] - 1] = V_k[j] - last_element_v_k
                    last_element_v_k = V_k[j]
        res_row.append(row_add)

    res_row = np.array(res_row)

    sum_row = res_row.T @ np.ones(len(res_row))

    list_to_dictionary = []


    new_res_array = []
    for element in res_array:
        new_res_array.append(str(element))

    new_res_row = []
    for element in res_row:
        new_res_row.append(str(element))

    for i in range(len(res_array)):
        data_set = {"id": i, "contributions": new_res_array[i].replace(", ", " -> "), "player_sequence": new_res_row[i]}
        list_to_dictionary.append(data_set)

    data_set = {"id": len(res_array), "contributions": 'Вектор Шепли', "player_sequence": str(sum_row / len(res_array))}
    list_to_dictionary.append(data_set)

    return list_to_dictionary