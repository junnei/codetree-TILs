commands = list(input())

# R U L D
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
dir_num = 1

x, y = 0, 0
time = 0
answer = -1

for command in commands:
    if command == "L":
        dir_num = (dir_num + 1) % 4
        time += 1
    elif command == "R":
        dir_num = (dir_num + 3) % 4
        time += 1
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1
        if (x, y) == (0, 0):
            answer = time
            break

print(answer)