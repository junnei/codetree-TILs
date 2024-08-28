n = int(input())

# dp[n] : 정수 n을 1, 2, 5 의 합으로 나타내는 방법의 수.
nums = [1, 2, 5]
dp = [
    0 for _ in range(n+1)
]

for i in range(1, n+1):
    for num in nums:
        if i-num >= 0:
            dp[i] += dp[i-num]
        if i == num:
            dp[i] += 1
print(dp[-1]%10007)