import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = INT_MIN

for i in range(n):
    for j in range(n-2):
        sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if sum_val > max_val:
            max_val = sum_val
print(max_val)