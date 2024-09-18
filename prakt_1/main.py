a = 17
b = 1
x = 1
n = 30
values = []

for i in range(n):
    x = ((a*x + b) % 1000)
    u = x / 1000
    print(round(u,2))
