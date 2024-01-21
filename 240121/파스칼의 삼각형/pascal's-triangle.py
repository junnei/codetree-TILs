import sys

input = sys.stdin.readline

n = int(input())

result = [
    [1] * n
    for _ in range(n)
]

for i in range(2, n):
    for j in range(1, i):
        result[i][j] = result[i-1][j] + result[i-1][j-1]

for i in range(n):
    print(*result[i][:i+1])