from basic import mean, median, mode

_ = int(input())
arr = sorted(map(int, input().split()))

print(mean(arr))
print(median(arr))
print(mode(arr))
