import sys

input = sys.stdin.readline

n, m = map(int,input().split())

result = [
    [0] * m
    for _ in range(n)
]

cnt = 0

for i in range(n+m-1):
    for j in range(max(0,i-m+1), min(n, i+1)):
        cnt += 1
        result[j][i-j] = cnt

for i in range(n):
    print(*result[i])