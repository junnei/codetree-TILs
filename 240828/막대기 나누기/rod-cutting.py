n = int(input())
lines = list(map(int, input().split()))

# dp[n] : 길이의 합이 n일 때 최대의 가치.
dp = [
    0 for _ in range(n+1)
]

for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-(j+1)] + lines[j])
print(dp[-1])