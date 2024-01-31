n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_min_distance(arr):
    sum_val = 0
    for i in range(len(arr) - 1):
        sum_val += get_distance(arr[i], arr[i+1])
    return sum_val

import sys

answer = sys.maxsize
for i in range(1, n-1):
    n_arr = arr[:i] + arr[i+1:]
    result = get_min_distance(n_arr)
    if result < answer:
        answer = result
print(answer)