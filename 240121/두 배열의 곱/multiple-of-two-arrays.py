import sys

input = sys.stdin.readline

n = 3
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
_ = input()
arr2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    print(*[arr[i][j] * arr2[i][j] for j in range(n)])