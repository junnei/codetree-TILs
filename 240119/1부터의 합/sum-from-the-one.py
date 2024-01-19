import sys

input = sys.stdin.readline

n = int(input())
sum_val = 0

for i in range(1,n+1):
    sum_val += i
    if sum_val >= n:
        print(i)
        break