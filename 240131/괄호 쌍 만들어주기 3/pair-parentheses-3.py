import sys

INT_MAX = sys.maxsize

arr = list(input())
n = len(arr)

cnt = 0
for i in range(n):
    if arr[i] == "(":
        for j in range(i, n):
            if arr[j] == ")":
                cnt += 1

print(cnt)