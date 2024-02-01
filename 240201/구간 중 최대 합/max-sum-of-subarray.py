n, k = map(int, input().split())
arr = list(map(int, input().split()))

import sys
INT_MIN = -sys.maxsize

max_val = INT_MIN

for i in range(n-k+1):
    sum_val = 0
    for j in range(k):
        sum_val += arr[i+j]
    if sum_val > max_val:
        max_val = sum_val

print(max_val)