import math
from typing import List


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
