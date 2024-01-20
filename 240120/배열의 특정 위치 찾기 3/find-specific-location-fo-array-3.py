import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

index = 0
for i in range(len(arr)):
    if arr[i] == 0:
        index = i
        break

print(arr[index-1] + arr[index-2] + arr[index-3])