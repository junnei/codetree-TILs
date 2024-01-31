n, t = map(int, input().split())

commands = list(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def move(x, y, direction, cnt):
    global answer
    if commands[cnt] == "R":
        direction = (direction + 1) % 4
    elif commands[cnt] == "L":
        direction = (direction - 1 + 4) % 4
    elif in_range(x, y):
        nx, ny = x + dxs[direction], y + dys[direction]
        if in_range(nx, ny):
            answer += arr[x][y]
            return nx, ny, direction, cnt + 1
    return x, y, direction, cnt + 1

dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

def simulate(x, y, direction, cnt):
    global answer
    while in_range(x, y) and cnt < t:
        x, y, direction, cnt = move(x, y, direction, cnt)
    answer += arr[x][y]

answer = 0
x, y, direction = n//2, n//2, 1
simulate(x, y, direction, 0)

print(answer)