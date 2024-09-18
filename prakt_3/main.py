# Оценка качества генераторов псевдослучайных чисел

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

from abc import ABC, abstractmethod

class GeneratorEvaluator:
    @staticmethod
    def math_expectance(_func_random_generator: Callable, _iterations_amount=1_000_000):
        _random_values = []
        for _i in _func_random_generator(_iterations_amount):
            _random_values.append(_i)
        print(f"мат ожидание для {_func_random_generator.__name__} Равно M = {sum(_random_values) / len(_random_values)}")

    @staticmethod
    def dispersion(_func_random_generator: Callable, _iterations_amount=1_000_000):
    # массив элементов, из каждого числа вычитаем мат ожидание и возводим в квадрат, а сумму элементов делим на количество числе -1
    # Должно быть 0.0833333333
        _diviations = []
        for _i in _func_random_generator(_iterations_amount):
            _diviations.append((_i - 0.5)**2)
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
    def math_expectance(_random_values : List):
        return sum(_random_values) / len(_random_values)

    @staticmethod
    def dispersion(_random_values : List):
    # массив элементов, из каждого числа вычитаем мат ожидание и возводим в квадрат, а сумму элементов делим на количество числе -1
    # Должно быть 0.0833333333
    # только для
        _M = ListEvaluator.math_expectance(_random_values)
        _diviations = []
        for _i in _random_values:
            _diviations.append((_i - _M)**2)
        return sum(_diviations) / (len(_diviations) - 1)

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

    @staticmethod
    def periodic_evaluator():
        pass

class Generators:
    @staticmethod
    def basic_generator_random(_n):
        for _i in range(_n):
            yield random()

    @staticmethod
    def reccurent_method(_n):
        _a = 17 # множитель
        _x = 1
        for _i in range(_n):
            _x = ((_a * _x + 1) % 1000)
            _U = _x / 1000
            yield _U

    @staticmethod
    def muli_metod(_n):
        _a = 22695477
        _m = 2**32
        _x = 1
        for _i in range(_n):
            _x = ((_a * _x + 1) % _m)
            _U = _x / _m
            yield _U

# print("Метод random()")
# Evaluator.math_expectance(Generators.basic_generator_random)
# Evaluator.dispersion(Generators.basic_generator_random)
# Evaluator.periodic_evaluator(Generators.basic_generator_random)

print()
print("Мультипликационный метод")
GeneratorEvaluator.math_expectance(Generators.muli_metod)
GeneratorEvaluator.dispersion(Generators.muli_metod)
GeneratorEvaluator.periodic_evaluator(Generators.muli_metod)

















