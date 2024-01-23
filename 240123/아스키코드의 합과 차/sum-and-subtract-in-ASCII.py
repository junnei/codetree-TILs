import sys

input = sys.stdin.readline

a, b = map(ord, input().rstrip().split())

print(a+b, abs(a-b))