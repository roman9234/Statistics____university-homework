import scipy.stats as sts

x = [[3.83, 3.0, 2.7],
     [4.1, 3.13, 3.5],
     [3.63, 3.6, 3.2],
     [3.27, 3.5, 3.7]]
# x = [[3, 7, 3, 6, 6, 7, 6, 3, 8, 3],
#      [6, 5, 7, 4, 9, 4, 3, 2, 7, 8],
#      [8, 6, 3, 2, 7, 8, 6, 9, 3, 8],
#      [4, 7, 7, 8, 6, 4, 5, 8, 4, 7],
#      [6, 2, 6, 6, 8, 9, 7, 6, 8, 1]]
k = len(x[0])
m = len(x)
xi = [0 for i in range(k)]
xj = [0 for j in range(m)]
_x = 0
S02 = 0
SnA2 = 0
SnB2 = 0
SA2 = 0
SB2 = 0
A = False
B = False
for i in range(k):
    for j in range(m):
        _x += x[j][i]
        xj[j] += x[j][i] / k
        xi[i] += x[j][i] / m
_x = _x / k
_x = _x / m
# print(xi)
# print(xj)
# print(_x)

for i in range(k):
    for j in range(m):
        S02 += (x[j][i] - xi[i]) ** 2
for j in range(m):
    S02 -= k * ((xj[j] - _x) ** 2)
S02 /= ((k - 1) * (m - 1))
print(f'случайный фактор {S02}')
for i in range(k):
    SnA2 += (xi[i] - _x) ** 2
SnA2 *= m / (k - 1)
print(f'выборочная дисперсия А {SnA2}')
for j in range(m):
    SnB2 += (xj[j] - _x) ** 2
SnB2 *= k / (m - 1)
print(f'выборочная дисперсия В {SnB2}')

F = sts.f.ppf(0.95, (k - 1), (k - 1) * (m - 1))
if (SnA2 / S02) > F:
    print('фактор А значимый и вот он')
    SA2 = (SnA2 - S02) / m
    print(SA2)
    A = True
else:
    print('фактор А не значимый')

F = sts.f.ppf(0.95, (m - 1), (k - 1) * (m - 1))
if (SnB2 / S02) > F:
    print('фактор B значимый и вот он')
    SB2 = (SnB2 - S02) / k
    print(SB2)
    B = True
else:
    print('фактор B не значимый')

if not A and not B:
    print('все факторы не значимы поэтому оцениваем генеральную дисперсию')
    S2 = ((k - 1) * SnA2 + (m - 1) * SnB2 + (k - 1) * (m - 1) * S02) / ((k - 1) + (m - 1) + (k - 1) * (m - 1))
    print(S2)
if A and not B:
    print('фактор B не значим, оцениваем генеральную дисперсию')
    S2 = (m - 1) * SnB2 + (k - 1) * (m - 1) * S02 / ((m - 1) + (k - 1) * (m - 1))
    print(S2)
if B and not A:
    print('фактор A не значим, оцениваем генеральную дисперсию')
    S2 = (k - 1) * SnA2 + (k - 1) * (m - 1) * S02 / ((k - 1) + (k - 1) * (m - 1))
    print(S2)
