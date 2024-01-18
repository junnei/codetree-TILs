import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]
sum_val = 0
cnt = 0
for num in nums:
    if num >= 0 and num <= 200:
        sum_val += num
        cnt += 1
print(sum_val, round(sum_val/cnt,1))