n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


#   Up Right Down Left
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

answer = 0

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1
print(answer)