import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_val = +sys.maxsize
max_val = -sys.maxsize

for num in arr:
    if num < min_val:
        min_val = num
    if num - min_val > max_val:
        max_val = num - min_val

print(max_val)