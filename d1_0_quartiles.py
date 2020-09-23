from basic import median, split_half

_ = int(input())
arr = sorted(map(int, input().split()))

# import numpy as np
# print(np.median(arr[:size >> 1]))
# print(np.median(arr))
# print(np.median(arr[(size + 1) >> 1:]))

front, end = split_half(arr)
print(int(median(front)))
print(int(median(arr)))
print(int(median(end)))
