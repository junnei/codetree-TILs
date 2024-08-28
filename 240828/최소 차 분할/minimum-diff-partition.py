n = int(input())
nums = list(map(int, input().split()))

MAX_VAL = sum(nums)//2
remain = sum(nums)%2
# n개의 수가 주어졌을 때, 이를 둘로 나눈 합 간의 차이
# dp[n] : 무게의 합이 M일 때 최대의 가치.
dp = [
    0 for _ in range(MAX_VAL+1)
]

for num in nums:
    for i in range(MAX_VAL, num, -1):
        if dp[i-num] != 0:
            dp[i] = max(dp[i], dp[i-num] + 1)
    if dp[num] == 0:
        dp[num] = 1
        
answer = remain
for val in dp[::-1]:
    if val == 0:
        answer += 1
    else:
        break
print(answer)