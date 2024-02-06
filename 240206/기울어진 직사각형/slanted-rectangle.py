n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]


def get_sum_num(x, y, i, j):
    sum_val = 0
    cnts = [i, j, i, j]
    for dx, dy, cnt in zip(dxs, dys, cnts):
        for _ in range(cnt):
            x, y = x + dx, y + dy
            sum_val += arr[x][y]
    return sum_val

def get_max_num(a, b):
    max_val = 0
    for i in range(1, n):
        for j in range(1, n):
            if 0 <= a-(i+j) < n and j <= b < n-i:
                max_val = max(max_val, get_sum_num(a, b, i, j))
    return max_val

max_val = 0
for i in range(2, n):
    for j in range(1, n-1):
        max_val = max(max_val, get_max_num(i, j))
print(max_val)