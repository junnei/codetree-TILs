arr = [
    list(map(int, str(input())))
    for _ in range(3)
]

MAX_SIZE = 9

import sys

def can_win(a, b):
    for i in range(3):
        if arr[i][0] in (a, b) and arr[i][1] in (a, b) and arr[i][2] in (a, b):
            if not arr[i][0] == arr[i][1] == arr[i][2]:
                return True

    for i in range(3):
        if arr[0][i] in (a, b) and arr[1][i] in (a, b) and arr[2][i] in (a, b):
            if not arr[0][i] == arr[1][i] == arr[2][i]:
                return True

    if arr[0][0] in (a, b) and arr[1][1] in (a, b) and arr[2][2] in (a, b):
        if not arr[0][0] == arr[1][1] == arr[2][2]:
            return True
     
    if arr[2][0] in (a, b) and arr[1][1] in (a, b) and arr[0][2] in (a, b):
        if not arr[2][0] == arr[1][1] == arr[0][2]:
            return True
    return False

cnt = 0
for i in range(1, MAX_SIZE+1):
    for j in range(i+1, MAX_SIZE+1):
        if can_win(i, j):
            cnt += 1

print(cnt)