import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

for num in nums:
    if num%2 == 1 and num%3 ==0:
        print(num)