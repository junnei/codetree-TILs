n, m = map(int, input().split())
nums = list(map(int, input().split()))

INT_MAX = 101

# dp[m] : 수열 내 원소의 합이 m이 되게 하는 최소 수열의 길이.
dp = [
    INT_MAX for _ in range(m+1)
]

for num in nums:
    for i in range(m, num, -1) :
        if dp[i-num] != INT_MAX:
            dp[i] = min(dp[i], dp[i-num] + 1)
    dp[num] = 1
print(-1 if dp[-1]==INT_MAX else dp[-1])