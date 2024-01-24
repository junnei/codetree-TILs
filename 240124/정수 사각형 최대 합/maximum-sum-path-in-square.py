import sys

input = sys.stdin.readline

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0] * n
    for _ in range(n)
]

dp[0][0] = arr[0][0]

def is_range(a, b):
    return (0 <= a and a < n) and (0 <= b and b < n)

def get_max(a, b):
    if not is_range(a, b):
        return 0
    if dp[a][b] != 0:
        return dp[a][b]
    else:
        dp[a][b] = max(get_max(a-1, b), get_max(a, b-1)) + arr[a][b]
        return dp[a][b]

print(get_max(n-1, n-1))