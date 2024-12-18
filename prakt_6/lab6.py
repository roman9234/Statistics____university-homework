import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm, t, chi2

# from lab5 import task
a = [[5, 10, 15, 30, 40, 50]]
M = [10]
S = [2]

#task(0.1, a_list)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
alpha = "ABCDEFGHIJKLMNOPQ"
P = [.1, .05, .02, .01]

for i in range(1):
    data = [f"p = {P[i]}"]
    p = P[i]
    for j in range(1):
        offset = (2 + 7 * i, 1 + 4 * j)
        data.append(f"M = {M[j]}")
        data.append("")
        data.append(f"S = {S[j]}")
        data.append("")
    ws.append(data)
    data = [""]
    for j in range(1):
        offset = (3 + 7 * i, 1 + 4 * j)
        data.append("Гаусс")
        data.append("")
        data.append("хи2")
        data.append("")
    ws.append(data)
    data = [""]
    for j in range(1):
        offset = (4 + 7 * i, 1 + 4 * j)
        data.append("M_max")
        data.append("M_min")
        data.append("S_max")
        data.append("S_min")
    ws.append(data)
    data = [""]
    for j in range(1):
        offset = (5 + 7 * i, 1 + 4 * j)
        data.append(M[j] + norm.ppf(1 - p/2, 0, 1) * S[j] / len(a[j]) ** .5)
        data.append(M[j] - norm.ppf(1 - p/2, 0, 1) * S[j] / len(a[j]) ** .5)
        print("Пределы гаусса:", data[-2], data[-1])
        data.append(S[j] * ((len(a[j]) - 1) / chi2.ppf(p/2, len(a[j]) - 1)) ** .5)
        data.append(S[j] * ((len(a[j]) - 1) / chi2.ppf(1 - p/2, len(a[j]) - 1)) ** .5)
        print("Пределы хи квадрат:", data[-2], data[-1])
    ws.append(data)
    data = [""]
    for j in range(1):
        offset = (6 + 7 * i, 1 + 4 * j)
        data.append("Стьюдент")
        data.append("")
        data.append("")
        data.append("")
    ws.append(data)
    data = [""]
    for j in range(1):
        offset = (7 + 7 * i, 1 + 4 * j)
        data.append("M_max")
        data.append("M_min")
        data.append("")
        data.append("")
    ws.append(data)
    data = [""]
    for j in range(1):
        offset = (8 + 7 * i, 1 + 4 * j)
        
        data.append(M[j] + t.ppf(1 - p/2, len(a[j]) - 1) * S[j] / len(a[j]) ** .5)
        data.append(M[j] - t.ppf(1 - p/2, len(a[j]) - 1) * S[j] / len(a[j]) ** .5)
        print("Пределы Стьюдента:", data[-2], data[-1])
        data.append("")
        data.append("")
    ws.append(data)
        

wb.save("table_example.xlsx")



def N(x, m=10, sigma=2):
    return (1 / (sigma*math.sqrt(2*math.pi)) ) * math.exp(-((x-m)**2)/(2*sigma**2) )

def func(x):
    integral, error = quad(N, -float('inf'), x)
    return integral

def getArg(f, minArg, maxArg, value, eps):
    minVal = f(minArg)
    maxVal = f(maxArg)

    while abs((maxArg-minArg)/maxArg)>eps:
        midArg = (minArg+maxArg)/2
        midVal = f(midArg)
        if midVal > value:
            maxArg = midArg
            maxVal = midVal
        else:
            minArg = midArg
            minVal = midVal
    return (minArg+maxArg)/2

# Сравнение
print(getArg(func, 0, 20, 0.95, 10**(-15)))
print(norm.ppf(0.95, 10, 2))

def getTabF(f, minArg, maxArg, pointsCount):
    minVal = f(minArg)
    maxVal = f(maxArg)
    dVal = (maxVal-minVal)/(pointsCount-1)
    yTab = [minVal]
    xTab = [minArg]
    for i in range(1, pointsCount-2):
        yTab.append(minVal + dVal*i)
        xTab.append(getArg(f, minArg, maxArg, yTab[i], 10**(-15)))
    yTab.append(maxVal)
    xTab.append(maxArg)
    res = [xTab, yTab]
    return res

def model_N(xTab, yTab, p):
    y = 20 * p
    for i in range(1, len(xTab)-1):
        if yTab[i-1]<=p<=yTab[i]:
            y = ((p-yTab[i])/(yTab[i-1]-yTab[i]))*xTab[i-1]+((p-yTab[i-1])/(yTab[i]-yTab[i-1]))*xTab[i]
            break
    return y

def getFreqDistr(paramsArr, A, B, intervalsCount):
    dY = (B-A)/intervalsCount
    freq = []
    for i in range(0, intervalsCount):
        freq.append(0)
    for j in range(0, len(paramsArr)):
        Yc = paramsArr[j]
        fN = math.floor(Yc/dY)
        freq[fN] += 1
    for i in range(0, intervalsCount):
        freq[i] = freq[i]/(len(paramsArr)*dY)
    return freq

ms = [10, 10, 10, 12]
sigmas = [2, 0.5, 1, 1]

colors = ['r', 'g', 'b', 'orange']

for i in range(4):
    m = ms[i]
    sigma = sigmas[i]
    ys = []
    xs = np.linspace(0, 20, 1000)
    for x in xs:
        ys.append(N(x, m, sigma))
    plt.plot(xs, ys, label=f"N(x, {m}, {sigma})", color=colors[i])

plt.title(f"Функция плотности нормального закона", fontsize=15)
plt.legend(loc='center left', bbox_to_anchor=(-0.4, 0.87))
plt.show()

xs = np.linspace(0, 20, 1000)
ys = []
for x in xs:
    ys.append(func(x))
plt.title(f"Функция распределения", fontsize=15)    
plt.plot(xs, ys, label=f"func(x)", color='r')
plt.show()

min_v = 0
max_v = 20
tabSize = 1001
TAB_XY = getTabF(func, min_v, max_v, tabSize)
xTab, yTab = TAB_XY[0], TAB_XY[1]

plt.title(f"Табличная функция распределения вероятности", fontsize=15)
plt.plot(xTab, yTab, label=f"Tab", color='r')
plt.show()


ps = np.linspace(0, 1, 10000)
ys = []
for p in ps:
    ys.append(model_N(xTab, yTab, p))

plt.title(f"Функция для кусочной аппроксимации", fontsize=15)
plt.plot(ps, ys, label=f"Model_N(XTab, YTab, p)", color='r')
plt.show()

errors = []

for degree in range(3, 7):
    expNmb = 10**degree
    patArr_e3 = []
    for j in range(expNmb-1):
        patArr_e3.append(model_N(xTab, yTab, random.random()))
    # print(patArr_e3)
    # print(max(patArr_e3))
    # print(min(patArr_e3))
    print(patArr_e3)
    print(len(patArr_e3))
    


    A = min_v
    B = max_v
    K = 100
    resX = []
    
    for k in range(0, K):
        resX.append(((B-A)/K)*(0.5+k))
    resY = getFreqDistr(patArr_e3, A, B, K)
    resY[-1] = 0

    error = 0
    for i in range(0, K):
        error += ((N(resX[i], 10, 2)-resY[i])**2)/K
    errors.append(error)    

    # print(resX)
    # print(len(resX))
    # print(resY)


    ys = []
    for x in resX:
        ys.append(N(x, 10, 2))
    plt.plot(resX, ys, label=f"N(x, m, sigma)", color='r')
    plt.title(f"Гистограмма относительных частот. Длина:10^{degree}", fontsize=15)
    plt.bar(resX, resY, 0.2, edgecolor = 'black')
    plt.show()
print("Отклонения:")
for error in errors:
    print(error)
plt.plot([3, 4, 5, 6], errors, label=f"Зависимость среднеквадратического отклонения от длины последовательности", color='r')
plt.xlabel("Длина последовательности (10^i)")