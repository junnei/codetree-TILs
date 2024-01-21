import sys

input = sys.stdin.readline

n = int(input())

for i in range(n,0,-1):
    print(*[i+j*n if j % 2 == 0 else n+1-i+j*n for j in range(n-1,-1,-1)])