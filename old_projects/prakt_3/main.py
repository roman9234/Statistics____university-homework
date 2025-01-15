# Оценка качества генераторов псевдослучайных чисел
import math
# Тесты - их будет 3
# 1 - оценка совпадения математического ожидания и дисперсии нашего генератора
# соотвтетственно с теоретическим значением равномерного рамрпед
# мат ожидание [0,1] равно M=0.5
# дисперсия равна D=1/12

# 2 - оценка периодичности последовательности.
# берём первое число, и в цикле по остальным сравниваем со всеми другими, далее третье, и так далее

# 3 - оценка равномерности распределения случайных чисел. (?)
# получаем плотность распределения вероятностей P(x) - размерная еличина

# 4 - считаем величину "хи квадрат"
# вероятность совпадения 0.7-0.9


# 5


from typing import Callable, List
from random import random

import matplotlib.pyplot as plt
import numpy as np

from abc import ABC, abstractmethod


class GeneratorEvaluator:
    @staticmethod
    def math_expectance(_func_random_generator: Callable, _iterations_amount=1_000_000):
        _random_values = []
        for _i in _func_random_generator(_iterations_amount):
            _random_values.append(_i)
        print(
            f"мат ожидание для {_func_random_generator.__name__} Равно M = {sum(_random_values) / len(_random_values)}")

    @staticmethod
    def dispersion(_func_random_generator: Callable, _iterations_amount=1_000_000):
        # массив элементов, из каждого числа вычитаем мат ожидание и возводим в квадрат, а сумму элементов делим на количество числе -1
        # Должно быть 0.0833333333
        _diviations = []
        for _i in _func_random_generator(_iterations_amount):
            _diviations.append((_i - 0.5) ** 2)
        print(f"Дисперсия {_func_random_generator.__name__} Равна D = {sum(_diviations) / (len(_diviations) - 1)}")

    @staticmethod
    def periodic_evaluator(_func_random_generator: Callable, _iterations_amount=1_000_000):
        _random_values = []
        _i = 0
        for _n in _func_random_generator(_iterations_amount):
            _random_values.append(_n)
            _i += 1
            if _random_values[0] == _random_values[-1] and _i != 1:
                print(f"Оченка периодичности - числа повторяются примерно раз в {_i} значений")
                return
        else:
            print(f"Значения повторяются реже, чем раз в {_iterations_amount}")


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
    def frequency_evaluator(_a: int, _b: int, _interval_count: int, _random_values: List):
        result = [x for x in range(10)]
        return result


class Generators:

    @staticmethod
    def get_list_from_generator(_func_random_generator: Callable, _iterations_amount=1_000_000):
        return [x for x in _func_random_generator(_iterations_amount)]

    @staticmethod
    def get_list_with_intervals(_a: int, _b: int, _func_random_generator: Callable, _iterations_amount=1_000_000):
        return [_a + x * (_b - _a) for x in _func_random_generator(_iterations_amount)]

    @staticmethod
    def random_module_generator(_n):
        for _i in range(_n):
            yield random()

    # мультипликационный метод
    @staticmethod
    def muli_metod(_n):
        _a = 22695477
        _m = 2 ** 32
        _x = 1
        for _i in range(_n):
            _x = ((_a * _x + 1) % _m)
            _U = _x / _m
            yield _U


# print("Метод random()")
# Evaluator.less_than_p_value(Generators.basic_generator_random)
# Evaluator.dispersion(Generators.basic_generator_random)
# Evaluator.periodic_evaluator(Generators.basic_generator_random)

# print("оценка списков")
# print(ListEvaluator.less_than_p_value(Generators.get_list_from_generator(Generators.muli_metod)))
# print(ListEvaluator.dispersion(Generators.get_list_from_generator(Generators.muli_metod)))
# ListEvaluator.periodic_evaluator(Generators.get_list_from_generator(Generators.muli_metod))

print("\nЗадание 1")
print(Generators.get_list_from_generator(Generators.muli_metod, _iterations_amount=10))

print("\nЗадание 2")
print(Generators.get_list_with_intervals(0, 10, Generators.muli_metod, _iterations_amount=10))

print("\nЗадание 3")
GeneratorEvaluator.math_expectance(Generators.muli_metod)
GeneratorEvaluator.dispersion(Generators.muli_metod)

print("\nЗадание 4")
GeneratorEvaluator.periodic_evaluator(Generators.muli_metod)

print("\nЗадание 5-6")
bins = 10
iterations = 100
x = Generators.get_list_with_intervals(0, 10, Generators.muli_metod, _iterations_amount=iterations)
plt.hist(x, density=True, bins=bins)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data')
plt.show()

print("\nЗадание 7")

import numpy as np
from scipy.stats import chisquare

observed_data = Generators.get_list_with_intervals(0,10,Generators.muli_metod,_iterations_amount=1000)

# Рассчитываем наблюдаемые частоты для каждого числа (от 0 до 10)
observed_frequencies = [0 for x in range(10)]
for x in observed_data:
    q = math.ceil(x)
    observed_frequencies[q-1] += 1

expected_frequencies = np.full(10, len(observed_data) / 10)

# Применяем критерий Пирсона через функцию
chi2_stat, p_value = chisquare(observed_frequencies, expected_frequencies)

# Критерий Пирсона (хи-квадрат) — это статистический тест,
# который используется для проверки гипотез о независимости или соответствии распределений.

# Вывод результатов
print(f"Статистика критерия Пирсона: {chi2_stat}")
print(f"p-значение: {p_value}")

if p_value < 0.05:
    print("Нулевая гипотеза отклоняется. Последовательность не соответствует равномерному распределению.")
else:
    print("Нулевая гипотеза не отклоняется. Последовательность соответствует равномерному распределению.")
