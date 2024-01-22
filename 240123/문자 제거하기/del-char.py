import sys

input = sys.stdin.readline

s = input().rstrip()

while len(s) - 1>0:
    n = int(input())
    if n > len(s) - 1:
        n = len(s) - 1
    s = s[:n]+s[n+1:]
    print(s)