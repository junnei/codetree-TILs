import sys

input = sys.stdin.readline

a, b, c = tuple(map(int, input().split()))

print(1 if b>a and b<c else 0)