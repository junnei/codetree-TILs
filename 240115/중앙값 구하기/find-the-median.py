import sys

input = sys.stdin.readline

nums = tuple(map(int, input().split()))

for num in nums:
    if num != min(nums) and num!= max(nums):
        print(num)