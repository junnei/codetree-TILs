n, m = map(int, input().split())
datas = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

arr = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
# R U L D
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

for x, y in datas:
    arr[x][y] = 1
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)