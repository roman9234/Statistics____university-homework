from random import randint
from ListEvaluator import ListEvaluator as Le

q = [randint(0,10) for i in range(10)]

print(Le.dispersion_old(q))
print(Le.dispersion(q))


