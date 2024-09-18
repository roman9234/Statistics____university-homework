import matplotlib.pyplot as plt
from math import pi
from random import random

def fpi(n):
    m = 0
    for q in range(n):
        xp = random() * (xmax - xmin) + xmin
        yp = random() * (ymax - ymin) + ymin
        yf = xp**3 + 1
        if yp <= yf:
            m += 1
    return (m/n) * (ymax - ymin) * (xmax - xmin)



xmin, xmax = 0, 2
ymin, ymax = 1, 9




exceptions_list = []
x_graph_values = []
# число экспериментов в цикле
i = 10**3
correct_surface_area = 6

while i <= 10**7:

    x_graph_values.append(i)
    integral_function = fpi(i)
    exceptions_list.append((abs(correct_surface_area - integral_function) / correct_surface_area) * 100)
    i *= 10
    print(integral_function)


plt.plot(x_graph_values,exceptions_list)
plt.semilogx ()
plt.show()
