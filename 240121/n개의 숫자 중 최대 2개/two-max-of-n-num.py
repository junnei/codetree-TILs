import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_val = -sys.maxsize
max_limit = -sys.maxsize

for num in arr:
    if num > max_limit:
        if num > max_val:
            max_val, max_limit = num, max_val
        else:
            max_limit = num
print(max_val, max_limit)