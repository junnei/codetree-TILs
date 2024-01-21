import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_diff = 99

for i in range(n):
    for j in range(i+1, n):
        if abs(arr[i] - arr[j]) < min_diff:
            min_diff = abs(arr[i] - arr[j])
print(min_diff)