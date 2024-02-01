n = 6
arr = list(map(int, input().split()))

sum_val = sum(arr)

import sys
min_diff = sys.maxsize

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            diff = abs(sum_val - 2 * (arr[i] + arr[j] + arr[k]))
            if diff < min_diff:
                min_diff = diff
print(min_diff)