import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]
cnt = [0, 0]
for num in nums:
    if num%3 == 0:
        cnt[0]+=1
    if num%5 ==0:
        cnt[1]+=1
print(*cnt)