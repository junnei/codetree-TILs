import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

x, y = max(a, b), min(a, b)

for i in range(x,y-1,step=-1):
    print(i, end=" ")