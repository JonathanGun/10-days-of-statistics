from geometry import geometry

nom, denom = map(int, input().split())
n = int(input())
prec = 3

print(round(geometry(n, nom / denom), prec))
