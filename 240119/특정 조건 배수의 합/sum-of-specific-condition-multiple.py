import sys

input = sys.stdin.readline

a, b = tuple(map(int,input().split()))

sum_val = 0

for i in range(min(a,b),max(a,b)+1):
    if i%5 == 0:
        sum_val += i
print(sum_val)