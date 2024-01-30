n = int(input())

arr = [list(input()) for _ in range(n)]

k = int(input()) - 1

dir_num, index = k // n, k % n
dxys = [[1, 0], [0, -1], [-1, 0], [0, 1]]
start_point = [[1, 1+index], [1+index, 3], [3, 3-index], [3-index, 1]]
x, y = start_point[dir_num]
dx, dy = dxys[dir_num]

def is_range(x, y):
    return 1<=x and x<=n and 1<=y and y<=n

cnt = 0
for _ in range(1000):
    if not is_range(x, y):
        break
    cnt += 1
    if arr[x-1][y-1] == "\\":
        dx, dy = dy, dx
    else:
        dx, dy = -dy, -dx
    x, y = x + dx, y + dy
print(cnt)