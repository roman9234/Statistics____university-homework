import matplotlib.pyplot as plt
from math import pi
from random import random

x0 = 1
y0 = 2
r0 = 5

def fpi(n):
    m = 0
    for q in range(n):
        xp = random() * (xmax - xmin) + xmin
        yp = random() * (ymax - ymin) + ymin
        d = (xp - x0) ** 2 + (yp - y0) ** 2
        if d <= r0**2:
            m += 1
    return 4 * (m / n)



xmin, xmax = x0-r0, x0+r0
ymin, ymax = y0-r0, y0+r0




exceptions_list = []
x_graph_values = []
# число экспериментов в цикле
i = 10**3

while i <= 10**7:
    x_graph_values.append(i)
    fp = fpi(i)
    exceptions_list.append((abs(pi - fp)/pi)*100)
    i *= 10
    print(fp)


plt.plot(x_graph_values,exceptions_list)
plt.semilogx ()
plt.show()
