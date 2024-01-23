import sys

input = sys.stdin.readline

a, b = input().rstrip().split()

print(int(a+b)+int(b+a))