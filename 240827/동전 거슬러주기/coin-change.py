n, m = map(int, input().split())
coins = list(map(int, input().split()))

import sys
INT_MAX = sys.maxsize

#dp[i] : 금액 i를 거슬러주기 위해 필요한 최소 동전의 수.

dp = [
    INT_MAX for _ in range(m+1)
]

for coin in coins:
    dp[coin] = 1

for i in range(1, m+1):
    for j in range(1, i):
        if dp[j] == INT_MAX:
            continue
        for coin in coins:
            if j + coin == i:
                dp[i] = min(dp[i], dp[j] + 1)

print(-1 if dp[-1] == INT_MAX else dp[-1])