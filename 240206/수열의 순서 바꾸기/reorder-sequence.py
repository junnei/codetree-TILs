n = int(input())
arr = list(map(int, input().split()))

cnt = 0
max_val = 0

import sys
if arr == sorted(arr):
    print(0)
    sys.exit()
for i in range(n):
    val = arr[0]
    if val > max_val:
        max_val = val
        arr.append(arr.pop(0))
        cnt += 1
    else:
        arr.insert((n-1)-(i+1),arr.pop(0))
print(cnt)