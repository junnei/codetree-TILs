import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

print(1 if a >= b else 0)
print(1 if a > b else 0)
print(1 if a <= b else 0)
print(1 if a < b else 0)
print(1 if a == b else 0)
print(1 if a != b else 0)