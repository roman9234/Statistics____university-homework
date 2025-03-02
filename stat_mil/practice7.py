from math import sqrt
import scipy.stats as sts


def find_mean(matrix):
    mean = 0
    for row in matrix:
        mean += sum(row)
    mean /= len(matrix) * len(matrix[0])
    return mean


def find_mean_row(matrix):
    m_j = []
    for row in matrix:
        m_j.append(sum(row)/len(row))
    return m_j


def find_mean_column(matrix):
    m_i = [0] * len(matrix[0])
    for row in matrix:
        for i in range(len(row)):
            m_i[i] += row[i]
    for i in range(len(m_i)):
        m_i[i] = m_i[i] / len(matrix)
    return m_i

def rand_factor(k, m, m_i, m_j, mean): # фактор случайности
    sum1 = 0
    sum2 = 0
    for i in range(m):
        for j in range(k):
            sum1 += (matrix[i][j] - m_i[j]) ** 2
    for j in range(m):
        sum2 += (m_j[j] - mean) ** 2
    s_0 = 1/((k - 1) * (m - 1)) * (sum1 - k * sum2)

    return s_0


def rand_a(k, m, m_i, mean):  # фактор случайности A
    sum_ = 0
    for i in range(k):
        sum_ += (m_i[i] - mean) ** 2
    s_nA = m/(k - 1) * sum_

    return s_nA

def rand_b(k, m, m_j, mean):  # фактор случайности B
    sum_ = 0
    for j in range(m):
        sum_ += (m_j[j] - mean) ** 2
    s_nB = k / (m - 1) * sum_

    return s_nB

def is_meaning_factor(p, s_n, s_0, f1, f2):
    return s_n / s_0 > sts.f.ppf(1 - p, f1, f2)

def meaningful_factor(s_n, s_0, n): # оценка факторов A или B, если фактор оказался значимым
    s_factor = (s_n - s_0) / n
    return s_factor

def general_dispersion_not_meaning_factor(s_n, s_0, n, k, m): # оценка генеральной дисперсии, если фактор A или B оказался незначимым
    s = ((n - 1) * s_n + (k - 1) * (m - 1) * s_0) / ((n - 1) + (k - 1) * (m - 1))
    return s

def general_dispersion(s_nA, s_nB, s_0, k, m): # оценка генеральной дисперсии, если оба фактора A и B оказались незначимыми
    s = ((k - 1) * s_nA + (m - 1) * s_nB + (k - 1) * (m - 1) * s_0) / ((k - 1) + (m - 1) + (k - 1) * (m - 1))
    return s

matrix = [[3.83, 3.00, 2.70],
          [4.10, 3.13, 3.50],
          [3.63, 3.60, 3.20],
          [3.27, 3.50, 3.70]]
k = len(matrix[0])  # количество столбцов
m = len(matrix)  # количество строк
p = 0.05

mean = find_mean(matrix)
m_j = find_mean_row(matrix)
m_i= find_mean_column(matrix)
s_0 = rand_factor(k, m, m_i, m_j, mean)
s_nA = rand_a(k, m, m_i, mean)
s_nB = rand_b(k, m, m_j, mean)
s_A, s_B, s = None, None, None

is_s_A_meaning = is_meaning_factor(p, s_nA, s_0, k - 1, (k - 1)*(m - 1))
is_s_B_meaning = is_meaning_factor(p, s_nB, s_0, m - 1, (k - 1)*(m - 1))

if is_s_A_meaning:
    s_A = meaningful_factor(s_nA, s_0, m)
else:
    s = general_dispersion_not_meaning_factor(s_nA, s_0, k, k, m)
if is_s_B_meaning:
    s_B = meaningful_factor(s_nB, s_0, k)
else:
    s = general_dispersion_not_meaning_factor(s_nB, s_0, m, k, m)
if not is_s_A_meaning and not is_s_B_meaning:
    s = general_dispersion(s_nA, s_nB, s_0, k, m)

print('S_0^2:', s_0)
print('S_nA^2:', s_nA)
print('S_nB^2:', s_nB)
print('S_A^2:', s_A)
print('S_B^2:', s_B)
print('S^2:', s)