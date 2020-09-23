mean = lambda arr: sum(arr) / len(arr)
avg = lambda arr, w=None: mean(arr) if not w else sum(i * j for i, j in zip(arr, w or [1] * len(arr))) / sum(w)
mid = lambda n: slice((n - 1) >> 1, (n >> 1) + 1)
median = lambda arr: avg(arr[mid(len(arr))])
mode = lambda arr: max(arr, key=arr.count)
stdev = lambda arr: (sum(map(lambda a: (a - mean(arr))**2, arr)) / len(arr)) ** 0.5
split_half = lambda arr: (arr[:len(arr) >> 1], arr[(len(arr) + 1) >> 1:])
