n, t = map(int, input().split())
r, c, d = input().split()

directions = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def is_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

index = directions[d]
r, c = map(int, (r, c))
for i in range(1, t+1):
    dx, dy = dxs[index], dys[index]
    nx, ny = r + dx, c + dy
    if is_range(nx, ny):
        r, c = nx, ny
    else:
        index = 3 - index
print(r, c)