n = int(input())

directions = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


MAX_T = 1000
pos = [[0, 0]] * MAX_T

x, y = 0, 0
answer = -1
time = 0

for i in range(n):
    dir_str, val_str = input().split()
    dir_num = directions[dir_str]
    val = int(val_str)

    while val > 0:
        time += 1
        val -= 1
        x, y = x + dxs[dir_num], y + dys[dir_num]
        pos[time] = [x, y]
        if (x, y) == (0, 0):
            answer = time
            break
    if answer != -1:
        break

print(answer)