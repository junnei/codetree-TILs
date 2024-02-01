n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

import sys

def in_range(x, y):
    return 0<=x<n and 0<=y<n

max_val = -sys.maxsize
size = 3

for i in range(n*n-size*2 + 1):
    for j in range(i+size, n*n-size + 1):
        sum_val = 0
        for k in range(size):
            if in_range(i//n, i%n + k):
                sum_val += arr[i//n][i%n+k]
            else:
                sum_val = 0
                break
        if sum_val:
            for k in range(size):
                if in_range(j//n, j%n + k):
                    sum_val += arr[j//n][j%n+k]
                else:
                    sum_val = 0
                    break
        if sum_val > max_val:
            max_val = sum_val
print(max_val)