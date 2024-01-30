n = int(input())

arr = [list(input()) for _ in range(n)]

k = int(input())

directions = {
    1 : ([1, 1], [1, 0]),
    2 : ([1, 2], [1, 0]),
    3 : ([1, 3], [1, 0]),
    4 : ([1, 3], [0, -1]),
    5 : ([2, 3], [0, -1]),
    6 : ([3, 3], [0, -1]),
    7 : ([3, 3], [-1, 0]),
    8 : ([3, 2], [-1, 0]),
    9 : ([3, 1], [-1, 0]),
    10 : ([3, 1], [0, 1]),
    11 : ([2, 1], [0, 1]),
    12 : ([1, 1], [0, 1]),
}

(x, y), (dx, dy) = directions[k]

def is_range(x, y):
    return 1<=x and x<=n and 1<=y and y<=n

cnt = 0
while True:
    if not is_range(x, y):
        break
    cnt += 1
    if arr[x-1][y-1] == "\\":
        dx, dy = dy, dx
    else:
        dx, dy = -dy, -dx
    x, y = x + dx, y + dy
print(cnt)