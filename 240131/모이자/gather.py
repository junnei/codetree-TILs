import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_val = INT_MAX
for i in range(n):
    weighted_sum = 0
    for j in range(n):
        weighted_sum += arr[j] * abs(i-j)
    if weighted_sum < min_val:
        min_val = weighted_sum

print(min_val)