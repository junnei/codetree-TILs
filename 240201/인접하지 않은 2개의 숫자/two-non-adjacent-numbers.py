n = int(input())
arr = list(map(int, input().split()))

import sys

max_val = -sys.maxsize

for i in range(n):
    for j in range(i+2, n):
        sum_val = arr[i] + arr[j]
        if sum_val > max_val:
            max_val = sum_val
print(max_val)