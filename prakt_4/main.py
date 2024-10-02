import math
from random import randint
from typing import List
import matplotlib.pyplot as plt
import np


# T.normal(_n) = 2nd(k1) + 2nd(k2) + 2nd(k3) + 2nd(k4)
# _n  =10 20 50 100 200 10^3

# строим гистограмму мин-макс. делим на 10 интервалов
# узнаём как изменется характер чисел в зависимости от величин
# строим кривую

# 1/S * sqrt(2pi)

# k1 k2 k3 будут выданы каждому

# k1 = 2
# k2 = 1
# k3 = 7
# k4 = 3
class ListEvaluator:
    @staticmethod
    def math_expectance(_random_values: List):
        return sum(_random_values) / len(_random_values)

    @staticmethod
    def dispersion(_random_values: List):
        # массив элементов, из каждого числа вычитаем мат ожидание и возводим в квадрат, а сумму элементов делим на количество числе -1
        # Должно быть 0.0833333333
        # только для
        _M = ListEvaluator.math_expectance(_random_values)
        _diviations = []
        for _i in _random_values:
            _diviations.append((_i - _M) ** 2)
        return sum(_diviations) / (len(_diviations) - 1)

    @staticmethod
    def periodic_evaluator(_random_values: List):
        for _n in range(len(_random_values)):
            if _random_values[0] == _random_values[_n] and _n != 0:
                print(f"Оченка периодичности - числа повторяются примерно раз в {_n} значений")
                return _n
        else:
            print(f"Значения повторяются реже, чем раз в {len(_random_values)}")

    @staticmethod
    def sredne_kvadr(_random_values: List):
        return math.sqrt(ListEvaluator.dispersion(_random_values))

    @staticmethod
    def frequency_evaluator(_a: int, _b: int, _interval_count: int, _random_values: List):
        result = [x for x in range(10)]
        return result


print("\nЗадание 1")


# создаём функцию-генератор


class Generator:
    @staticmethod
    def get_t(k1=2, k2=1, k3=7, k4=3):
        return randint(0, k1) + randint(0, k2) + randint(0, k3) + randint(0, k4)

    @staticmethod
    def get_list(_n):
        return list(Generator.get_t() for _x in range(_n))


print(Generator.get_list(5))

print("\nЗадание 2-3")
# генерируем списки разной длины
n_values = [10, 20, 50, 100, 200, 500, 10 ** 3]
for n in n_values:
    print(f"\nn = {n}")
    generated_list = Generator.get_list(n)
    print(f"Мат ожидание равно {round(ListEvaluator.math_expectance(generated_list), 2)}")
    print(f"Дисперсия равна {round(ListEvaluator.dispersion(generated_list), 2)}")
    print(f"Среднеквадратическое отклонение {round(ListEvaluator.sredne_kvadr(generated_list), 2)}")
    print(Generator.get_list(n))

print("\nЗадание 4")
import numpy as np

# n_values = [10,20,50,100,200,500,10**3]
n_values = [10]
for n in n_values:
    bins = 10
    x = Generator.get_list(100)
    mean = ListEvaluator.math_expectance(x)
    std_dev = ListEvaluator.sredne_kvadr(x)
    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) ** np.exp(-((x - mean)**2) / (2 * std_dev ** 2))
    plt.plot(x,y)
    plt.show()

    # plt.hist(x, density=True, bins=bins)  # density=False would make counts
    # plt.ylabel('Probability')
    # plt.xlabel('Data')
    # plt.show()

print("\nЗадание 5")

print("\nЗадание 6")

print("\nЗадание 7")

print("\nЗадание 8")

print("\nЗадание 9")
