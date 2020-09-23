from binom import binom

a, b = map(float, input().split())
p = a / (a + b)
n = 6
x = 3
prec = 3
print(round(sum(binom(i, n, p) for i in range(x, n + 1)), prec))
