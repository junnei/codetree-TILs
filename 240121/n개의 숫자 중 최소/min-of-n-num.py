import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_val = sys.maxsize
min_cnt = 0

for num in arr:
    if num < min_val:
        min_val = num
        min_cnt = 1
    elif num == min_val:
        min_cnt += 1
print(min_val, min_cnt)