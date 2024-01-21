import sys

input = sys.stdin.readline

n = int(input())

result = [
    [1] * n
    for i in range(n)
]

for i in range(1, n):
    for j in range(1, n):
        result[i][j] = result[i-1][j] + result[i][j-1] + result[i-1][j-1]

for i in range(n):
    print(*result[i])