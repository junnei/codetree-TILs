import sys

input = sys.stdin.readline

s = input().rstrip()

print(s.replace(s[1], s[0]))