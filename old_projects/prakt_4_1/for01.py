# Используем другие последовательности случайных числе
from math import sqrt, exp, pi
from random import randint, random
from typing import List

from ListEvaluator import ListEvaluator


# NA(n,p)
# Функция гарантирует частоты
# p = 0.5

# Эта программа генерирует последовательности, которые имеют другой характер распределения

# Надо выделить некое Nкритическое число, для того чтобы уйти от этого начального участка
# Оно задаётся в виде начальных данных - 50 100 200 - значения для Nкритического

# На этом значении прогоняем случайные числа 10 20 50

# Линейный закон

# От Amin до Amax

def how_often(_list: List, _max=1, _min=0, _intervals_amount=10):
    # _intervals = [x + 1 for x in range(len(_list))]
    delta = (_max-_min) / _intervals_amount
    _frequencies_borders = [x * delta for x in range(1, _intervals_amount + 1)]
    _frequencies = [0 for x in range(1,_intervals_amount + 1)]
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





import matplotlib.pyplot as plt
less_than_p_values_list = []

n_values = [50,100,200]




# p = 0.5
p = 0.1
n = 1000
m = 0



random_values_list = []
for i in range(1,n+1):
    ui = random()
    if ui < p:
        m+=1
    less_than_p_value = m / i
    random_values_list.append(ui)
    less_than_p_values_list.append(less_than_p_value)

    if i in n_values:
    # if i == 50:
        # -------- Реальные M и D --------
        # среднеквадр. отклонение
        average_mistake = ListEvaluator.sredne_kvadr(random_values_list)
        print(f"Среднекв отклонение = {average_mistake}")
        # мат ожидание
        math_expectance = ListEvaluator.math_expectance(random_values_list)
        print(f"Мат ожидание = {math_expectance}")
        # Функция распределения
        expected = [(1 / (average_mistake * sqrt(2 * pi))) * exp(
            -((x / 10 - math_expectance) ** 2) / (2 * (average_mistake ** 2))
        ) / 10 for x in range(0, 110)]


        fig, ax = plt.subplots(1, 2, width_ratios=(3.0,4.0))
        plot1 = ax[0]
        plot2 = ax[1]

        plot1.set_ylim(0,1)
        plot2.set_xlim(0,1)
        plot2.set_ylim(0,0.4)

        plot1.set_yticks([x/10 for x in range(10)])
        plot1.plot(list(range(i)), [0.5 for x in range(i)], color="y")
        plot1.plot(list(range(i)), less_than_p_values_list)

        frequencies_borders, frequencies = how_often(random_values_list)

        print(sum(frequencies))

        plot2.set_xticks(frequencies_borders)
        plot2.plot([x / 10 for x in range(110)], expected, color="r")
        plot2.bar(frequencies_borders, frequencies,width=0.1)
        plot2.plot([x / 10 for x in range(110)], expected, color="r")

        plt.show()


