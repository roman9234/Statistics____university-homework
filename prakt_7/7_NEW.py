from scipy import stats

table = [
    [3, 7, 3, 6, 6, 7, 6, 3, 8, 3],
    [6, 5, 7, 4, 9, 4, 3, 2, 7, 8],
    [8, 6, 3, 2, 7, 8, 6, 9, 3, 8],
    [4, 7, 7, 8, 6, 4, 5, 8, 4, 7],
    [6, 2, 6, 6, 8, 9, 7, 6, 8, 1]
]


# table = [
#     [3.83, 3.0, 2.7],
#     [4.1, 3.13, 3.5],
#     [3.63, 3.6, 3.2],
#     [3.27, 3.5, 3.7]
# ]

# ТЕСТОВАЯ ВЫБОРКА
# table = [
#     [1,2,3],
#     [2,2,2],
#     [3,4,5]
# ]

# Длина строки
k = len(table[0])
# Высота столбца
m = len(table)

# X_IJ
# Средние по строкам номер J (горизонтальной)
x_j_avers = []
# Средние по столбцам номер I (вертикальному)
x_i_avers = []

# Подсчет средних по строкам
for j in range(m): # для каждой строки
    summ = 0
    for i in range(k): # для каждого столбца
        summ += table[j][i]
    x_j_avers.append(summ / k)

# Подсчет средних по стоолбцам
for i in range(k): # для каждого столбца
    summ = 0
    for j in range(m): # для каждой строки
        summ += table[j][i]
    x_i_avers.append(summ / m)

# Получим среднее значение по всей таблице
t_summ = 0
for q in range(len(table)):
    t_summ += sum(table[q])
x_aver = t_summ/(k * m)

# Средние по строкам номер J (горизонтальной)
print(x_j_avers)
# Средние по столбцам номер I (вертикальному)
print(x_i_avers)
# Среднее всей таблицы
# print(x_aver)





# summ1 = 0
part_1 = 0
part_2 = 0
for j in range(m):
    # (среднее по строкам - среднее)^2
    part_2 += (x_j_avers[j]-x_aver)**2
    for i in range(k):
        part_1 += (table[j][i] - x_i_avers[i])**2
        # if i == 0:
        #     summ2 += (x_j_avers[j] - x_aver)**2

S_0_squared = (1 / ((k - 1) * (m - 1)))* (part_1 - k*part_2)
print(S_0_squared)

#
#
#
#
# s_0 = (1/((m-1)*(k-1))) * (summ1 - m*summ2)
# s_nA = (k/(m-1)) * summ3
# s_nB = (m/(k-1)) * summ2
#
#
# F_A = s_nA/s_0 # Чем больше F, тем значимее
# F_B = s_nB/s_0
#
# df1_A = m-1
# df1_B = k-1
# df2 = (m-1)*(k-1)
#
#
# p_value_A = stats.f.sf(F_A, df1_A, df2)
# p_value_B = stats.f.sf(F_B, df1_B, df2)
#
# # print(F_A, F_B, p_value_A, p_value_B, df1_A, df2)
# # print("S0 5.6","SnA 2.05", "0.36", "SnB 1.27", "0.22", "S 4.61")
#
# # Уровень значимости
# alpha = 0.05
# message_A = ""
# message_B = ""
# s = 0
# s_A = 0
# s_B = 0
#
# # Сопоставляем S_nA S_nB и S_0 по критерию Фишера
#
# # A
# if p_value_A < alpha:
#     s_A = (s_nA - s_0)/k
#     message_A = "значимый"
# else:
#     s = ((m-1)*s_nA+(m-1)*(k-1)*s_0)/((m-1)+(m-1)*(k-1))
#     message_A = "незначимый"
#
# # B
# if p_value_B < alpha:
#     s_B = (s_nB - s_0)/m
#     message_B = "значимый"
# else:
#     s = ((k-1)*s_nB+(m-1)*(k-1)*s_0)/((k-1)+(m-1)*(k-1))
#     message_B = "незначимый"
#
# if message_A == "незначимый" and message_B == "незначимый":
#     s = ((m-1)*s_nA+(k-1)*s_nB+(m-1)*(k-1)*s_0)/((m-1)+(k-1)+(m-1)*(k-1))
#
# print("S_0:", s_0)
# print("S_nA:", s_nA)
# print("S_nB:", s_nB)
# print("Задание на паре:", "S0 5.6","SnA 2.05","SnB 1.27", "S 4.61")
# if s_A != 0:
#     print("Оценка фактора А:", s_A)
#     print(s_A)
# if s_B != 0:
#     print("ОЦенка фактора B:", s_B)
#     print(s_B)
# if s != 0:
#      print(f"Фактор А {message_A} и фактор В {message_B}. Оценка генеральной дисперсии: {s}")
# # print(p_value_A)
# # print(p_value_B)
# 5.62












