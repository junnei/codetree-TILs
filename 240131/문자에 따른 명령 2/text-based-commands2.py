commands = list(input())
x, y = 0, 0

#   Up Right Down Left
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
index = 0

for command in commands:
    if command == "L":
        index = (index - 1) % 4
    elif command == "R":
        index = (index + 1) % 4
    else:
        x, y = x + dx[index], y + dy[index]
print(x, y)