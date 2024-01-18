import sys

input = sys.stdin.readline

n = int(input())
sum_val = 0
for i in range(n,100+1):
    sum_val += i
print(sum_val)