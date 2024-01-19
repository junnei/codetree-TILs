import sys

input = sys.stdin.readline

n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]

for a, b in nums:
    prod = 1
    for i in range(a, b+1):
        prod *= i
    print(prod)