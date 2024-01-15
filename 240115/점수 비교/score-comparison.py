import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

if a>c and b>d:
    print("1")
else:
    print("0")