n = int(input())

arr = [input() for _ in range(n)]

start_num = int(input())

def is_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def initialize(num):
    if num <= n:
        return 0, num - 1, 0
    elif num <= 2*n:
        return 1, n - 1, (num - n) - 1
    elif num <= 3*n:
        return 2, n - (num - 2*n), n - 1
    else:
        return 3, 0, n - (num - 3*n)

direction, x, y = initialize(start_num)
dx, dy = dxs[direction], dys[direction]

cnt = 0

def move(x, y, dx, dy):
    global cnt
    x, y = x + dx, y + dy
    if is_range(x, y):
        dx, dy = dxs[3-direction], dys[3-direction]
        move(x, y, dx, dy)
        cnt += 1

initialize(start_num)
move(x, y, dx, dy)

print(cnt)