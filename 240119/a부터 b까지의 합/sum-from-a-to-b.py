import sys

input = sys.stdin.readline

a, b = tuple(map(int,input().split()))

sum_val = 0

for i in range(a,b+1):
    sum_val += i
print(sum_val)