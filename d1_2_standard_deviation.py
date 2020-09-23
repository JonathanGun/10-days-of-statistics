from basic import stdev

_ = int(input())
print(round(stdev(list(map(int, input().split()))), 1))
