import sys

input = sys.stdin.readline

a, b, c = tuple(map(int, input().split()))

print(max(a, b, c))