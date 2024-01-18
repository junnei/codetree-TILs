import sys

input = sys.stdin.readline

b, a = tuple(map(int, input().split()))

if b%2 == 0:
    b -= 1
for i in range(b, a-1, step=-2):
    print(i, end=" ")