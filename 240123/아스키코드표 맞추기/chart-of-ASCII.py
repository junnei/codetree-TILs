import sys

input = sys.stdin.readline

values = list(map(lambda x : chr(int(x)), input().rstrip().split()))

print(*values)