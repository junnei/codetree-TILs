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

def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

x, y = 0, 0
arr[x][y] = 1

for i in range(2, n*m+1):
    nx, ny = x + dxs[index], y + dys[index]

    if not (is_range(nx, ny) and arr[nx][ny] == 0):
        index = (index + 1) % 4
    
    x, y = x + dxs[index], y + dys[index]
    arr[x][y] = i

for col in arr:
    print(*col)