n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

def move(x, y, direction, cnt):
    arr[x][y] = chr(cnt)
    nx, ny = x + dxs[direction], y + dys[direction]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        return nx, ny, direction, cnt + 1
    else:
        nd = (direction + 1) % 4
        nx, ny = x + dxs[nd], y + dys[nd]
        return nx, ny, nd, cnt + 1

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def simulate(x, y, direction, cnt):
    while in_range(x, y) and arr[x][y] == 0:
        x, y, direction, cnt = move(x, y, direction, cnt)

x, y, direction = 0, 0, 0
simulate(x, y, direction, ord("A"))

for col in arr:
    print(*col)