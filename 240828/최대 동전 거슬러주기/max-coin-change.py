n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [
    -1 for _ in range(m+1)
]

dp[0] = 0

for i in range(1, m+1):
    for coin in coins:
        if i-coin < 0:
            continue
        if dp[i-coin] == -1:
            continue
        dp[i] = max(dp[i], dp[i-coin] + 1)
print(dp[-1])