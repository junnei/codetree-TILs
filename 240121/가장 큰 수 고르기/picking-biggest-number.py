import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

max_val = -sys.maxsize

for num in arr:
    if num > max_val:
        max_val = num
print(max_val)