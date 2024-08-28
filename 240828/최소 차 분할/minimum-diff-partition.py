n = int(input())
nums = list(map(int, input().split()))

MAX_VAL = sum(nums)
# n개의 수가 주어졌을 때, 이를 둘로 나눈 합 간의 차이
# dp[n] : 무게의 합이 M일 때 최대의 가치.
dp = [
    0 for _ in range((MAX_VAL + 1)//2 + 1)
]

for num in nums:
    for i in range((MAX_VAL + 1)//2, num, -1):
        if dp[i-num] != 0:
            dp[i] = max(dp[i], dp[i-num] + 1)
    if dp[num] == 0:
        dp[num] = 1

answer = MAX_VAL
for i, num in enumerate(dp):
    if 0 < num < n:
        answer = min(answer, abs(MAX_VAL - 2 * i))
print(answer)