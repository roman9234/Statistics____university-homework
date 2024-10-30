from math import sqrt
import numpy as np
from scipy.stats import norm as qnorm, t as qt, chi, chi2

from ListEvaluator import ListEvaluator as Le

# На следующее занятие
# Оценка среднего и дисперсии выборки
# К следующему занятию все библиотеки освоить
# На лекции расскажет библиотеки, которые надо усвоить

# Вариант 5 работы: 4

# Оценка результатов наблюдений

# Будет 4 выборки

n1 = 4
n2 = 6
n3 = 10
n4 = 12

# Расчитываем по формуле 4 оценку генерального среднего
# Xm оцениваем по формуле 1
# Генеральнй стандарт по формуле 3

# Квантиль нормального распределения P
# P = 0.1
# 0.05
# 0.02
# 0.01


# U 1-(p/2) = U0.95

# Генеральны стандарт заменяем выборочным, которы расчитывается по формуле 3

# Задание 1

a41 = [9.245, 10.172, 12.718, 6.167]
a42 = [9.919, 12.095, 5.811, 5.706, 12.016, 9.259]
a43 = [17.346, 5.909, 13.688, 6.508, 13.619, 5.948, 12.476, 7.664, 11.896, 12.354]
a44 = [5.359, 13.891, 10.171, 9.256, 16.561, 10.498, 9.716, 14.094, 9.558, 18.492, 12.564, 6.576]

print("Задание 2")

print()
print(a41)
print(f"Мат ожидание: {round(Le.math_expectance(a41), 3)}")
print(f"Дисперсия: {round(Le.dispersion(a41), 3)}")
print(f"Среднеквадратическое отклонение: {round(Le.sredne_kvadr(a41), 3)}")

print()
print(a42)
print(f"Мат ожидание: {round(Le.math_expectance(a42), 3)}")
print(f"Дисперсия: {round(Le.dispersion(a42), 3)}")
print(f"Среднеквадратическое отклонение: {round(Le.sredne_kvadr(a42), 3)}")

print()
print(a43)
print(f"Мат ожидание: {round(Le.math_expectance(a43), 3)}")
print(f"Дисперсия: {round(Le.dispersion(a43), 3)}")
print(f"Среднеквадратическое отклонение: {round(Le.sredne_kvadr(a43), 3)}")

print()
print(a44)
print(f"Мат ожидание: {round(Le.math_expectance(a44), 3)}")
print(f"Дисперсия: {round(Le.dispersion(a44), 3)}")
print(f"Среднеквадратическое отклонение: {round(Le.sredne_kvadr(a44), 3)}")

print()
print("Задание 3")
print()



# Заданный список чисел
# data = [10, 12, 14, 15, 18, 21, 22, 23, 25]
data = [10.73, 5.88, 9.245, 10.172]


def quantiles(lst: list, p: float = 0.1):
    # Уровень значимости p

    # Количество степеней свободы для распределения Стьюдента df это n-1, где n - размер выборки
    df = len(lst) - 1
    print()
    print(lst)

    # Граничные квантили для нормального распределения
    lower_quantile_norm = qnorm.ppf(p / 2)
    upper_quantile_norm = qnorm.ppf(1 - p / 2)

    print("Нормальное распределение:")
    print(f"Нижний квантиль: {round(lower_quantile_norm, 3)}")
    print(f"Верхний квантиль: {round(upper_quantile_norm, 3)}")

    # Граничные квантили для распределения Стьюдента
    lower_quantile_t = qt.ppf(p / 2, df)
    upper_quantile_t = qt.ppf(1 - p / 2, df)

    print("\nРаспределение Стьюдента:")
    print(f"Нижний квантиль: {round(lower_quantile_t, 3)}")
    print(f"Верхний квантиль: {round(upper_quantile_t, 3)}")

# Для уровня значимости 0.1
quantiles(a41)
quantiles(a42)
quantiles(a43)
quantiles(a44)

print()
print("Задание 4")
print()

def dover_intervals(lst: list, p:float = 0.1):

    print(lst)

    # нижний предел для нормального закона
    print(f"\nНижний предел для нормального закона: ", end="")
    a_min = Le.math_expectance(lst) - qnorm.ppf(1-p/2)*(Le.sredne_kvadr(lst)/sqrt(len(lst)))
    print(a_min, end="")

    # нижний предел для Стьютента
    print(f"\nНижний предел для Стьютента: ", end="")
    a_min_t = Le.math_expectance(lst) - qt.ppf(1-p/2, len(lst) - 1)*(Le.sredne_kvadr(lst)/sqrt(len(lst)))
    print(a_min_t, end="")

    # верхний предел для нормального закона
    print(f"\nВерхний предел для нормального закона: ", end="")
    a_max = Le.math_expectance(lst) + qnorm.ppf(1 - p / 2) * (Le.sredne_kvadr(lst) / sqrt(len(lst)))
    print(a_max, end="")

    # верхний предел для Стьютента
    print(f"\nВерхний предел для Стьютента: ", end="")
    a_max_t = Le.math_expectance(lst) + qt.ppf(1 - p / 2, len(lst) - 1) * (Le.sredne_kvadr(lst) / sqrt(len(lst)))
    print(a_max_t, end="")

dover_intervals(a44)

print()
print("Задание 5")
print()


print("Граничные квантили хи квадрат")

def gran_kvan(lst: list, p:float = 0.1):
    print(chi2.ppf(1 - p / 2, len(lst) - 1))
    print(chi2.ppf(p / 2, len(lst) - 1))

gran_kvan(a44)


print()
print("Задание 6")
print()

def dover_intervals(lst: list, p:float = 0.1):
    s_min_2 = ((Le.sredne_kvadr(lst)**2)*(len(lst)-1)) / (chi2.ppf(1 - p / 2, len(lst) - 1))
    print(s_min_2)

dover_intervals(a44)





