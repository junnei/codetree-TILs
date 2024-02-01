import sys 

MAX_POS = 101

n, k = map(int, input().split())
arr = [0 for _ in range(MAX_POS)]

for i in range(n):
    val, pos = map(int, input().split())
    arr[pos] += val

import sys

MIN_INT = -sys.maxsize

max_val = MIN_INT

for i in range(min(50, k), max(51, MAX_POS-k)):
    cnt = sum(arr[i-k:i+k+1])
    if cnt > max_val:
        max_val = cnt
print(max_val)