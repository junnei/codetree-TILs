import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_diff = 99

for i in range(1, n):
    if arr[i] - arr[i-1] < min_diff:
        min_diff = arr[i] - arr[i-1]
print(min_diff)