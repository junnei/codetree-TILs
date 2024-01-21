import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = [
    [0] * (n+1)
    for _ in range(n+1)
]

for i in range(1, m+1):
    r, c = list(map(int, input().split()))
    result[r][c] = i

for i in range(1, n+1):
    print(*result[i][1:])