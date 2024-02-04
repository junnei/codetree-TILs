n, m = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations

max_val = max(arr)

for limit in range(5000):
    if max_val > limit:
        continue
    sum_val = 0
    cnt = 0
    for i in range(n):
        sum_val = sum_val + arr[i]
        if sum_val > limit:
            cnt += 1
            sum_val = arr[i]
    if cnt <= m-1:
        print(limit)
        break