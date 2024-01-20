import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    if i == 0:
        break
    cnt += 1

print(sum(arr[:cnt]), round(sum(arr[:cnt])/cnt, 1))