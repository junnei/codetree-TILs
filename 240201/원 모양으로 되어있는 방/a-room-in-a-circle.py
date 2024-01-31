n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

import sys

min_val = sys.maxsize

def get_min_distance(start):
    sum_val = 0
    for i in range(n):
        distance = i-start if i>=start else n-start+i
        sum_val += arr[i] * distance
    return sum_val

for i in range(n):
    result = get_min_distance(i)
    if result < min_val:
        min_val = result
print(min_val)