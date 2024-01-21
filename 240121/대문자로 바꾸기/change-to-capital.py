import sys

input = sys.stdin.readline

n = 5
arr = [
    list(input().split())
    for _ in range(n)
]

for i in range(n):
    print(*[char.upper() for char in arr[i]])