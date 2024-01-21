import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

arr = [
    [
        list(map(int, input().split()))
        for _ in range(n)
    ] for _ in range(2)
]

result = [
    [0] * m
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr[0][i][j] != arr[1][i][j]:
            result[i][j] = 1

for i in range(n):
    print(*result[i])