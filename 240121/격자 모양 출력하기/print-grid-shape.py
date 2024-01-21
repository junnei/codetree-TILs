import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = [
    [0] * (n+1)
    for _ in range(n+1)
]

for _ in range(m):
    r, c = list(map(int, input().split()))
    result[r][c] = r*c

for i in range(1, n+1):
    print(*result[i][1:])