n, s = map(int, input().split())
arr = list(map(int, input().split()))

import sys

min_diff = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        sum_val = sum(arr[:i])+sum(arr[i+1:j])+sum(arr[j+1:])
        diff = abs(sum_val - s)
        if diff < min_diff:
            min_diff = diff
print(min_diff)