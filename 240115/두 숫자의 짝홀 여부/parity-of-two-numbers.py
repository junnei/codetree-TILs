import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")