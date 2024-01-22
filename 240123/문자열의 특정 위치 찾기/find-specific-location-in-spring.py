import sys

input = sys.stdin.readline

arr = input().rstrip().split()

result = arr[0].find(arr[-1])

if result == -1:
    print("No")
else:
    print(result)