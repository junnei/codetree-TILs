import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    if i == 0:
        break
    cnt += 1

sum_val = 0
sum_cnt = 0

for i in arr[:cnt]:
    if i%2 == 0:
        sum_val += i
        sum_cnt += 1
print(sum_cnt, sum_val)