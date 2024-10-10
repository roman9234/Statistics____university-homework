import math
from random import randint
import matplotlib.pyplot as plt

from math import sqrt, pi, exp
from typing import List

import numpy as np


# T.normal(_n) = 2nd(k1) + 2nd(k2) + 2nd(k3) + 2nd(k4)
# _n  =10 20 50 100 200 10^3

# строим гистограмму мин-макс. делим на 10 интервалов
# узнаём как изменется характер чисел в зависимости от величин
# строим кривую

# 1/S * sqrt(2pi)

# k1 k2 k3 будут выданы каждому


def how_often(_list: List, _max=13, _min=0, _intervals_amount=13):
    # _intervals = [x + 1 for x in range(len(_list))]
    delta = _max / _intervals_amount
    _frequencies_borders = [x * delta for x in range(0, _intervals_amount + 1)]
    _frequencies = [0 for x in range(_intervals_amount + 1)]
    for x in _list:
        _i = 0
        while True:
            if x <= _frequencies_borders[_i]:
                _frequencies[_i] += 1
                break
            _i += 1

    for _i in range(len(_frequencies)):
        _frequencies[_i] = _frequencies[_i] / (len(_list))

    for _i in range(len(_frequencies_borders)):
        _frequencies_borders[_i] -= delta / 2

    return _frequencies_borders, _frequencies


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

print("\nЗадание 4-9")

rnd_values_list = Generator.get_list(1000)

frequencies_borders, frequencies = how_often(rnd_values_list, _intervals_amount=9)
print(sum(frequencies))
# -------- Реальные M и D --------
# среднеквадр. отклонение
q = ListEvaluator.sredne_kvadr(rnd_values_list)
# мат ожидание
m = ListEvaluator.math_expectance(rnd_values_list)
# Функция распределения
expected = [(1 / (q * sqrt(2 * pi))) * exp(
    -((x / 10 - m) ** 2) / (2 * (q ** 2))
) for x in range(0, 140)]

plt.plot([x / 10 for x in range(140)], expected, color="r")

# -------- Теоретические M и D --------
k1 = 2
k2 = 1
k3 = 7
k4 = 3
# среднеквадр. отклонение
q = math.sqrt(
    (((k1 - 0) ** 2) / 12 + ((k2 - 0) ** 2) / 12 + ((k3 - 0) ** 2) / 12 + ((k4 - 0) ** 2) / 12)
)

# мат ожидание
m = (k1 + k2 + k3 + k4) / 2
# Функция распределения
expected = [(1 / (q * sqrt(2 * pi))) * exp(
    -((x / 10 - m) ** 2) / (2 * (q ** 2))
) for x in range(0, 140)]

plt.plot([x / 10 for x in range(140)], expected, color="g")
plt.xticks(frequencies_borders)
plt.bar(frequencies_borders, frequencies)

plt.show()
