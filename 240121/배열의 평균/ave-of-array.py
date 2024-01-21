import sys

input = sys.stdin.readline

n = 2
size = 4
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

print(*[round(sum(arr[i]) / size, 1) for i in range(n)])
print(*[round(sum([arr[i][j] for i in range(n)]) / n, 1) for j in range(size)])
print(round(sum([sum(arr[i]) for i in range(n)]) / (n * size), 1))