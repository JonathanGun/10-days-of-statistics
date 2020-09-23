nom, denom = map(int, input().split())
p = nom / denom
q = 1 - p
n = int(input())
prec = 3

print(round(1 - q**n, prec))
