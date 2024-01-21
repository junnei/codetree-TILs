import sys

input = sys.stdin.readline

arr = list(map(len, [input().rstrip() for _ in range(3)]))
max_val = max(arr)
min_val = min(arr)
print(max_val - min_val)