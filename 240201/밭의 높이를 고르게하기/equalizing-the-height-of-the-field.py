n, h, t = map(int, input().split())

arr = list(map(int, input().split()))

import sys
min_val = sys.maxsize

for i in range(n-t+1):
    cost = 0
    for j in range(t):
        cost += abs(arr[i+j]-h)
    if cost < min_val:
        min_val = cost
print(min_val)