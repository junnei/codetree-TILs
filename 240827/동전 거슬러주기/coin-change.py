n, m = map(int, input().split())
coins = [
    coin for coin in map(int, input().split())
    if coin <= m
]
    

import sys
INT_MAX = sys.maxsize

#dp[i] : 금액 i를 거슬러주기 위해 필요한 최소 동전의 수.

dp = [
    INT_MAX for _ in range(m+1)
]

for coin in coins:
    dp[coin] = 1

for i in range(1, m+1):
    for coin in coins:
        if 0 >= i - coin:
            continue
        if dp[i - coin] == INT_MAX:
            continue
        
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(-1 if dp[-1] == INT_MAX else dp[-1])