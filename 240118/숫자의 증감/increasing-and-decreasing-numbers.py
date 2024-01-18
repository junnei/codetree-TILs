import sys

input = sys.stdin.readline

c, n = list(input().split())

for i in sorted(range(int(n)), reverse=True if c =="D" else False):
    print(i+1, end=" ")