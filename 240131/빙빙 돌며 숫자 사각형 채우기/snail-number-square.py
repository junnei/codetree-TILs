n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

directions = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3
}
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

index = 0
cnt = 1

def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def colorize(x, y):
    global cnt
    global index
    if is_range(x, y) and arr[x][y] == 0:
        arr[x][y] = cnt
        cnt += 1
        for dx, dy in zip(dxs[index:]+dxs[:index], dys[index:]+dys[:index]):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and arr[nx][ny] == 0:
                return nx, ny
            else:
                index = (index + 1) % 4

    return False

x, y = 0, 0
while True:
    work = colorize(x, y)
    if work == False:
        break
    x, y = work

for col in arr:
    print(*col)