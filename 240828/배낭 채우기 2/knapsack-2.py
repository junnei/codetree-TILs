n, m = map(int, input().split())
items = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp[m] : 무게의 합이 M일 때 최대의 가치.
dp = [
    0 for _ in range(m+1)
]

for i in range(1, m+1):
    for w, v in items:
        if i-w < 0:
            continue
        dp[i] = max(dp[i], dp[i-w] + v)
print(dp[-1])