import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

for i in range(n):
    print(*range(i*m + 1, i*m+m + 1))