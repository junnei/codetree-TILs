import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(*[i+j*n+1 for j in range(n)])