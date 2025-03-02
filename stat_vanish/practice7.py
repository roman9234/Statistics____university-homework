import scipy.stats as sts

# Исходные
# Sk - Swg
# Sa = Sbg
# k - кол-во столбцов
# m - кол-во рядов
tab = [[3.83, 3.0, 2.7],
       [4.1, 3.13, 3.5],
       [3.63, 3.6, 3.2],
       [3.27, 3.5, 3.7]]

Ms_columns = [sum([tab[j][i] for j in range(len(tab))]) / len(tab) for i in range(len(tab[0]))]
Ms_rows = [sum([tab[i][j] for j in range(len(tab[0]))]) / len(tab[0]) for i in range(len(tab))]
M_all = sum([sum(row) for row in tab]) / (len(tab) * len(tab[0]))
print("M_all = " + str(M_all))
print("Ms_columns = " + str(Ms_columns))
print("Ms_rows = " + str(Ms_rows))

k = len(tab[0])
m = len(tab)

Swg_columns = 0
for i in range(len(tab[0])):
    for j in range(len(tab)):
        Swg_columns += (tab[j][i] - Ms_columns[i])**2
print("Swg_columns = " + str(round(Swg_columns * 1000) / 1000))

Sbg_rows = 0
for j in range(len(tab)):
    Sbg_rows += (Ms_rows[j] - M_all)**2
print("Sbg_rows = " + str(round(Sbg_rows * 1000) / 1000))

Sbg_columns = sum([(Ms_columns[i] - M_all)**2 for i in range(len(tab[0]))])
print("Sbg_columns = " + str(round(Sbg_columns * 1000) / 1000))
print("\n----------------------------------\n")

# Задание 1
# Дисперсия фактора случайности
S0 = (1 / ((k - 1)*(m - 1))) * (Swg_columns - k*Sbg_rows)
print("S0 = " + str(round(S0 * 1000) / 1000))

# Задание 2
# Дисперсия влияния фактора А + дисперсия фактора случайности
# Значимость фактора А
Sna = (m / (k - 1)) * Sbg_columns
print("Sna = " + str(round(Sna * 1000) / 1000))

Fkr = sts.f.ppf(0.95, k - 1, (m - 1) * (k - 1))
print("Fkr = " + str(Fkr))
is_a_influence = (Sna / S0) > Fkr


# Задание 3
# Дисперсия влияния фактора B + дисперсия фактора случайности
# Значимость фактора Б
Snb = (k / (m - 1)) * Sbg_rows
print("Snb = " + str(round(Snb * 1000) / 1000))

Fkr = sts.f.ppf(0.95, m - 1, (m - 1) * (k - 1))
print("Fkr = " + str(Fkr))
is_b_influence = (Snb / S0) > Fkr


# Задание 4
if is_a_influence:
    # Оценка фактора А
    Sa = (Sna - S0) / m
    print("Sa = " + str(round(Sa * 1000) / 1000))
    print("Фактор А значим")
else:
    # Оценка ген дисперсии используя Sna и S0
    print("Фактор А не значим")
    S = ((k - 1)*Sna + (k - 1)*(m - 1)*S0) / ((k - 1) + (k - 1)*(m - 1))

# Задане 5
if is_b_influence:
    # Оценка фактора Б
    Sb = (Snb - S0) / k
    print("Фактор Б значим")
    print("Sb = " + str(round(Sb * 1000) / 1000))
else:
    # Оценка ген дисперсии используя Snb и S0
    print("Фактор Б не значим")
    S = ((m - 1)*Snb + (k - 1)*(m - 1)*S0) / ((m - 1) + (k - 1)*(m - 1))


# Задание 6
# Оценка ген дисперсии когда оба фактора не значимы
if not is_a_influence and not is_b_influence:
    S = ((k - 1)*Sna + (m - 1)*Snb + (k - 1)*(m - 1)*S0) / ((k - 1) + (m - 1) + (k - 1)*(m - 1))
    print("S = " + str(S))


if not is_a_influence and is_b_influence or not is_b_influence and is_a_influence:
    print("S = " + str(round(S * 1000) / 1000))
