from binom import binom

p, n = map(int, input().split())
p /= 100
x = 2
prec = 3
print(round(sum(binom(i, n, p) for i in range(x + 1)), prec))
print(round(sum(binom(i, n, p) for i in range(x, n + 1)), prec))
