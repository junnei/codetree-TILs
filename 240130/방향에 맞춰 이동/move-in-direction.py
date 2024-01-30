n = int(input())
x, y = 0, 0

directions = ["E", "S", "W", "N"]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    way, val = input().split()
    index = directions.index(way)
    x, y = x + dx[index]*int(val), y + dy[index]*int(val)
print(x, y)