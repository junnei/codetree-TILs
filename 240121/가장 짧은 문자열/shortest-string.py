import sys

input = sys.stdin.readline

arr = list(map(len, [input().rstrip() for _ in range(3)]))
print(max(arr) - min(arr))