import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

sum_val = 0
for num in nums:
    if num%3 == 0 and num%2 == 1:
        sum_val += num
print(sum_val)