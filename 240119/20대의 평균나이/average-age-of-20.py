import sys

input = sys.stdin.readline
sum_val = 0
cnt = 0
while True:
    n = int(input())
    if n//10 != 2:
        break
    sum_val += n
    cnt += 1
print(f"{sum_val/cnt:.2f}")