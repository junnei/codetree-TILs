import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

print(a*b if a>b else b//a)