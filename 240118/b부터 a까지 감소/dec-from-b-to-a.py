import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

for i in range(b, a-1, -1):
    print(i, end=" ")