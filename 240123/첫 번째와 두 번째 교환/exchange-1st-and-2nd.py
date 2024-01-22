import sys

input = sys.stdin.readline

arr = list(input().rstrip())

a, b = arr[0], arr[1]

for i in range(len(arr)):
    if arr[i] == a:
        arr[i] = b
    elif arr[i] == b:
        arr[i] = a
print(''.join(arr))