n = 5
arr = list(map(int, input().split()))

sum_val = sum(arr)

import sys
min_diff = sys.maxsize

found = False
for i in range(n-1):
    for j in range(i+1, n):
        for k in range(n-3):
            for l in range(k+1, n-2):
                temp_arr = (arr[:i]+arr[i+1:j]+arr[j+1:])
                a = (arr[i] + arr[j])
                b = (temp_arr[k] + temp_arr[l])
                c = sum_val - a - b
                if a == b or b == c or c == a:
                    continue
                diff = max(a, b, c) - min(a, b, c)
                if diff < min_diff:
                    min_diff = diff
                    found = True
if found:
    print(min_diff)
else:
    print(-1)