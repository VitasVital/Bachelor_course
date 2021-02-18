import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits


def unison_shuffle(a, b, c):
    assert len(a) == len(b) == len(c)
    p = np.random.permutation(len(a))

    return a[p], b[p], c[p]


def Softmax(W, x, b):
    x = np.reshape(x, (x.size, 1))
    U = W @ x + b
    U -= np.max(U)
    Max = np.exp(-np.max(U))
    V = (Max * np.exp(U)) / (Max * np.sum(np.exp(U)))

    return np.reshape(V, 10)


def Get_Y(W, X, b):
    Y = np.zeros((X[:, 0].size, 10))
    for i in range(Y[:, 0].size):
        Y[i] = Softmax(W, X[i], b)

    return Y


def Nabla_W(X, T, W, b):
    Y = Get_Y(W, X, b)
    nabla = (Y - T).T @ X

    return nabla


def Nabla_b(X, T, W, b):
    Y = Get_Y(W, X, b)
    nabla = (Y - T).T @ np.ones(X[:, 0].size)

    return np.reshape(nabla, (nabla.size, 1))


def Get_Error(X, T, W, b):
    error = 0
    Y = Get_Y(W, X, b)
    for i in range(X[:, 0].size):
        error -= np.log(Y[i, np.argmax(T[i])])

    return error


def Get_Accuracy(W, X, b, T):
    Total_True = 0
    for i in range(T[:,0].size):
        Total_True += (np.argmax(T[i]) == np.argmax(Softmax(W, X[i], b)))
    Accuracy = Total_True / X[:, 0].size

    return Accuracy


def main():
    digits = load_digits()

    # Стандартизация входных харрактеристик
    # Вычитаем вектор средних значений
    digits.data -= np.mean(digits.data, axis=0, dtype=np.float64)

    # Делим на вектор средних отклонений
    std = np.std(digits.data, axis=0, dtype=np.float64)
    for i in range(std.size):
        if std[i] == 0:
            std[i] = 1
    digits.data /= std

    # Перемешиваем, сохраняя соответствие меожу тремя массивами
    digits.data, digits.target, digits.images = unison_shuffle(digits.data, digits.target, digits.images)

    # Метки в виде One Hot - матрицы
    digits_oneHot = np.zeros(shape=(digits.data[:, 0].size, 10))
    for i in range(digits_oneHot[:, 0].size):
        digits_oneHot[i, digits.target[i]] = 1

    # Разбиваем на Train и Valid выборки
    length = digits.data[:, 0].size
    digits_data_train = digits.data[:int(length * 0.8)]
    digits_oneHot_train = digits_oneHot[:int(length * 0.8)]
    digits_data_valid = digits.data[int(length * 0.8):]
    digits_oneHot_valid = digits_oneHot[int(length * 0.8):]

    D = digits_data_train[0, :].size  # Размерность 1 вектора характеристик
    K = 10  # Кол-во классов

    # Инициализируем переменные для градиентного спуска
    dispersion = 0.05
    learn_rate = 0.001
    best_accuracy = 0
    best_W = None
    best_b = None
    total_iterations = 0
    W = np.random.normal(0, dispersion, size=(K, D))
    b = np.random.normal(0, dispersion, size=(K, 1))
    errors1 = []
    errors2 = []
    train_acc = [0,]
    valid_acc = [0,]

    # Цикл для градиентного спуска
    while True:
        # Градиент
        W -= learn_rate * Nabla_W(digits_data_train, digits_oneHot_train, W, b)
        b -= learn_rate * Nabla_b(digits_data_train, digits_oneHot_train, W, b)

        # Обновляем значение Accuracy на train сете
        cur_train_acc = Get_Accuracy(W, digits_data_train, b, digits_oneHot_train)

        if cur_train_acc > best_accuracy:
            # Обновляем всё остальное
            best_accuracy = cur_train_acc
            best_W = W
            best_b = b
            total_iterations += 1
            cur_train_Err = Get_Error(digits_data_train, digits_oneHot_train, W, b)
            cur_valid_Err = Get_Error(digits_data_valid, digits_oneHot_valid, W, b)
            cur_valid_acc = Get_Accuracy(W, digits_data_valid, b, digits_oneHot_valid)

            # Добавляем в список значения целевой функции, Accuracy на test и valid сетах
            errors1.append(cur_train_Err)
            errors2.append(cur_valid_Err)
            train_acc.append(cur_train_acc)
            valid_acc.append(cur_valid_acc)

            # Печать каждые 2 итерации
            if total_iterations % 2 == 0:
                print("=============================")
                print("Iteration # " + total_iterations.__str__())
                print("Train set:")
                print("E(W, b) = " + cur_train_Err.__str__())
                print("Accuracy = " + cur_train_acc.__str__())
                print("Valid set:")
                print("E(W, b) = " + cur_valid_Err.__str__())
                print("Accuracy = " + cur_valid_acc.__str__())

        else:
            break

    # Печать лучших метрик
    print("\n=============================")
    print("=============================")
    print("Best Accuracy: " + best_accuracy.__str__())
    print("Total iterations for learning: " + total_iterations.__str__())

    # Графики
    ox1 = np.arange(0, total_iterations)
    ox2 = np.arange(0, total_iterations + 1)

    plt.subplot(2, 2, 1)
    plt.title("E_train(iteration)")
    plt.plot(ox1, errors1)

    plt.subplot(2, 2, 2)
    plt.title("E_valid(iteration)")
    plt.plot(ox1, errors2)

    plt.subplot(2, 2, 3)
    plt.title("Accuracy on valid set(iteration)")
    plt.plot(ox2, valid_acc)

    plt.subplot(2, 2, 4)
    plt.title("Accuracy on train set (iteration)")
    plt.plot(ox2, train_acc)

    plt.show()


if __name__ == "__main__":
    main()
