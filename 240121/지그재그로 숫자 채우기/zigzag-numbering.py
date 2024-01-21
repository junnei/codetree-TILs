import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

for i in range(n):
    print(*[i+j*n if j%2==0 else n-1-i+j*n for j in range(m)])