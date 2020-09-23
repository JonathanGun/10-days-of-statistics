from basic import avg

_ = int(input())
arr = list(map(int, input().split()))
w = list(map(int, input().split()))

# import numpy as np
# print(np.average(arr, weights=w))

print(round(avg(arr, w), 1))
