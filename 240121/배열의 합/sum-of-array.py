import sys

input = sys.stdin.readline

n = 4
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    print(sum(arr[i]))