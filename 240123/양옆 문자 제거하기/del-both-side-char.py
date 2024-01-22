import sys

input = sys.stdin.readline

s = input().rstrip()

print(s[:1]+s[2:-2]+s[-1])