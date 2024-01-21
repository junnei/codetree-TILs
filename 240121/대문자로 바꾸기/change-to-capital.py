import sys

input = sys.stdin.readline

n = 5
arr = [
    list(input().split())
    for _ in range(n)
]

for i in range(n):
    print(*[chr(ord(char)-32) for char in arr[i]])