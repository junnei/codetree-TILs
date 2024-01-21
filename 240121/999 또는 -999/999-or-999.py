import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

min_val = sys.maxsize
max_val = -sys.maxsize

for num in arr:
    if num == 999 or num == -999:
        break
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(max_val, min_val)