n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
cnt = 0

def is_carry(num_arr):
    while len(num_arr):
        tmp_arr = []
        sum_val = 0
        for num in num_arr:
            if num // 10 > 0:
                tmp_arr.append(num//10)
            sum_val += num % 10
        if sum_val >= 10:
            return True
        num_arr = tmp_arr
    return False

import sys

max_val = -1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num_arr = [
                arr[i], arr[j], arr[k]
            ]
            if not is_carry(num_arr):
                if sum(num_arr) > max_val:
                    max_val = sum(num_arr)

print(max_val)