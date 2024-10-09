import random
from math import sqrt, pi, e, exp
from typing import List

import matplotlib.pyplot as plt

rnd_values_list = [random.randint(0, 13) for x in range(10)]
# rnd_values_list = [x for x in range(13)]


def how_often(_list: List, _max=13, _min = 0, _intervals_amount = 13):
    # _intervals = [x + 1 for x in range(len(_list))]
    delta = _max / _intervals_amount
    _frequencies_borders = [x*delta for x in range(0,_intervals_amount+1)]
    _frequencies = [0 for x in range(_intervals_amount+1)]
    for x in _list:
        _i = 0
        while True:
            if x <= _frequencies_borders[_i]:
                _frequencies[_i] += 1
                break
            _i+=1

    for _i in range(len(_frequencies)):
        _frequencies[_i] = _frequencies[_i] / len(_frequencies)



    return _frequencies_borders, _frequencies

frequencies_borders, frequencies = how_often(rnd_values_list)
# print(how_often(rnd_values_list))

disp = 7.23
# среднеквадр. отклонение
q = sqrt(disp)
# мат ожидание
m = 6.49

# expected = [x/100 for x in range(10)]
expected = [(1/(q*sqrt(2*pi)))*exp(
    -((x-m)**2) / (2*(q**2))
) for x in range(13+1)]

plt.plot(expected,color="r")

plt.xticks(frequencies_borders)
plt.bar(frequencies_borders, frequencies)

plt.show()
