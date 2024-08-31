n = int(input())
nums = [0] + list(map(int, input().split()))

m = sum(nums)

import sys
INT_MIN = -100

# dp[i][j] : i번째 수까지로 A-B로 j를 만들 수 있을때 A의 최대 합.
dp = [
    [INT_MIN] * (2 * m + 1)
    for _ in range(n + 1)
]

dp[0][m] = 0

for i in range(1, n+1):
    for j in range(0, 2*m+1):
        item = nums[i] # i 번쨰 수
        if 0 <= j-item and dp[i-1][j-item] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j-item] + item)
        if j+item <= 2*m and dp[i-1][j+item] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j+item])
        if dp[i-1][j] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[-1][m])