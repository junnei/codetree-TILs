n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [
    0 for _ in range(m+1)
]

for num in nums:
    for i in range(m, num, -1):
        if dp[i-num] != 0:
            dp[i] = max(dp[i], dp[i-num] + 1)
    if num <= m:
        dp[num] += 1
print("No" if dp[-1] == 0 else "Yes")