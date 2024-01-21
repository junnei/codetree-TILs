import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_val = -sys.maxsize

result = []

for idx, num in enumerate(arr):
    if num > max_val:
        result.append(idx+1)
        max_val = num

for i in result[::-1]:
    print(i, end=" ")