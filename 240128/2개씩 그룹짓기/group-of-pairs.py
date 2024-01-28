n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max_val = arr[0] + arr[-1]

for i in range(1, n):
    if arr[i] + arr[-(i+1)] > max_val:
        max_val = arr[i] + arr[-(i+1)]

print(max_val)