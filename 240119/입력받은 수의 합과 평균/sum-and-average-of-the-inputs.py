import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
print(sum(nums), round(sum(nums)/len(nums),1))