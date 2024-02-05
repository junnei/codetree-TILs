n = int(input())
arr = list(map(int, input().split()))

arr.sort()

import sys
min_diff = sys.maxsize

for i in range(n):
    diff = arr[n+i] - arr[i]
    min_diff = min(min_diff, diff)

print(min_diff)