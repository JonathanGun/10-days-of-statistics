from itertools import accumulate
import bisect

mean = lambda arr: sum(arr) / len(arr)
avg = lambda arr, w=None: mean(arr) if not w else sum(i * j for i, j in zip(arr, w or [1] * len(arr))) / sum(w)
mid = lambda n: slice((n - 1) >> 1, (n >> 1) + 1)

_ = int(input())
arr, f = zip(*sorted(zip(map(int, input().split()), map(int, input().split()))))

q2_idx = mid(sum(f))
q1_idx = mid(q2_idx.start if sum(f) % 2 == 1 else q2_idx.start + 1)
q3_idx = slice(q2_idx.stop + q1_idx.start, q2_idx.stop + q1_idx.stop)

f = list(accumulate(f))
q1 = mean([arr[bisect.bisect_right(f, q1_idx.start)], arr[bisect.bisect_right(f, q1_idx.stop - 1)]])
q3 = mean([arr[bisect.bisect_right(f, q3_idx.start)], arr[bisect.bisect_right(f, q3_idx.stop - 1)]])
print(round(q3 - q1, 1))
