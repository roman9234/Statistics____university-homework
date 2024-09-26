a = 22695477
b = 1
m = 2**32 
x0 = 1
A = 0
B = 10
M = (A+B)/2
D = ((B-A)**2)/12


def rand(a, b, m, x_i):
    return (a*x_i+b)%m

def randPeriod(X):
    result = []
    n = len(X)

    for i in range(n):
        element = X[i]
        for j in range(i, n):
            if (element == X[j]) and (i != j):
                result.append(j-i)
                result.append(i)
                result.append(j)
                return result
    result.append(-1)
    result.append(-1)
    result.append(-1)
    return result


for j in range(2, 6):
    N = 10**j
    numsArr = []
    paramsArr = []
    M_summ = 0
    D_summ = 0

    numsArr.append(rand(a, b, m, x0))

    for i in range(1, N):
        numsArr.append(rand(a, b, m, numsArr[i-1]))

    for i in range(N):
        numsArr[i] = numsArr[i]/m
        paramsArr.append(A + (B-A)*numsArr[i])
        M_summ += paramsArr[i]
        D_summ += paramsArr[i]**2
    M_j = M_summ/N
    D_j = ((D_summ/N) - M_j**2)*(N/(N-1))

    M_error = abs((M-M_j)/M)*100
    D_error = abs((D-D_j)/D)*100
    
    print(f"Длина последовательности:10^{j}:", paramsArr[:3])
    print("Макс:", max(paramsArr))
    print("Мин:", min(paramsArr))
    print("M:", M_j)
    print("D:", D_j)
    print("Погрешность M:", M_error)
    print("Погрешность D:", D_error)
    print("Тестирование на период:", randPeriod(paramsArr))
    print()




