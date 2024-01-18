import sys

input = sys.stdin.readline

c, n = list(input().split())

for i in range(1, int(n)+1, step=1 if c =='A' else -1):
    print(i, end=" ")