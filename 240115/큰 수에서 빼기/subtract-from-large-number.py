import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))
print(abs(a-b))