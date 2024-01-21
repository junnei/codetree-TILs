import sys

input = sys.stdin.readline

def uppercase(c: str):
    return c.upper()

n = 5
arr = [
    list(map(uppercase, input().split()))
    for _ in range(n)
]

for i in range(n):
    print(*arr[i])