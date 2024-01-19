import sys

input = sys.stdin.readline

n = int(input())
nums = [map(int, input().split()) for _ in range(n)]

for a, b in nums:
    sum_val = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            sum_val += i
    print(sum_val)