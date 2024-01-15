import sys

input = sys.stdin.readline

a, b, c = tuple(map(int, input().split()))

if a <= b and a <= c:
    print(a)
elif b <= c:
    print(b)
else:
    print(c)