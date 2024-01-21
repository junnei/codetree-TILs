import sys

input = sys.stdin.readline

n = 4
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

sum_val = 0
for i in range(n):
    for j in range(i+1):
        sum_val += arr[i][j]
print(sum_val)