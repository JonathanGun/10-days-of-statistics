fact = lambda n: 1 if n <= 1 else n * fact(n - 1)
comb = lambda n, c: fact(n) / fact(n - c) / fact(c)
binom = lambda x, n, p: comb(n, x) * p**x * (1 - p)**(n - x)
