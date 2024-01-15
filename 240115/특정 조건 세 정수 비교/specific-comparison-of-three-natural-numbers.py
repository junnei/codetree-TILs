import sys

input = sys.stdin.readline

a, b, c = tuple(map(int, input().split()))

print(1 if a < b and a < c else 0, 1 if a == b == c else 0)