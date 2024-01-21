import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

for num in arr:
    if num == 0:
        break
    if num % 2 == 0:
        print(num//2, end=" ")
    else:
        print(num+3, end=" ")