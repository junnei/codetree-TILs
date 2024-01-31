n = int(input())

arr = [input() for _ in range(n)]

start_num = int(input())

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def initialize(num):
    if num <= n:
        return 0, num - 1, 0
    elif num <= 2*n:
        return (num - n) - 1, n - 1, 1
    elif num <= 3*n:
        return n - 1, n - (num - 2*n), 2
    else:
        return n - (num - 3*n), 0, 3

def move(x, y, direction):
    nd = rotate_dict[arr[x][y]][direction]
    nx, ny = x + dxs[nd], y + dys[nd]
    return nx, ny, nd

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

rotate_dict = {
    "/" : [1, 0, 3, 2],
    "\\" : [3, 2, 1, 0]
}

def simulate(x, y, direction):
    cnt = 0
    while in_range(x, y):
        x, y, direction = move(x, y, direction)
        cnt += 1
    return cnt

x, y, direction = initialize(start_num)
answer = simulate(x, y, direction)

print(answer)