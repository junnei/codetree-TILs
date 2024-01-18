import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

if a>0:
    for i in range(b):
        print(a, end="")
else:
    print(0)