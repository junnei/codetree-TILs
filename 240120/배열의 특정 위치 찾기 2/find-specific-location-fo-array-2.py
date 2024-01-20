import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

sum_odd = 0
sum_even = 0

for i in range(len(arr)):
    if i % 2 == 0:
        sum_even += arr[i]
    else:
        sum_odd += arr[i]

print(sum_even - sum_odd if sum_even > sum_odd else sum_odd - sum_even)