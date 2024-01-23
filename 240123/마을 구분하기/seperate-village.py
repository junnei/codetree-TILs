import sys

input = sys.stdin.readline

n = int(input().rstrip())
visited = [[False for _ in range(n+1)] for _ in range(n+1)]

board = [
    [0 for _ in range(n+1)],
    *[[0, *list(map(int, input().split()))] for _ in range(n)]
    ]

def is_range(a, b):
    if (1<=a and a<=n) and (1<=b and b<=n):
        return True
    else:
        return False

def is_available(a, b):
    if not is_range(a, b):
        return False
    if board[a][b] == 0:
        return False
    if visited[a][b] == True:
        return False
    return True

def dfs(a, b):
    global cnt
    dxys = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in dxys:
        x, y = a + dx, b + dy
        if is_available(x, y):
            visited[x][y] = True
            cnt += 1
            dfs(x, y)

result = []
cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if is_available(i, j):
            visited[i][j] = True
            cnt += 1
            dfs(i, j)
            result.append(cnt)
            cnt = 0

print(len(result))

for i in sorted(result):
    print(i)