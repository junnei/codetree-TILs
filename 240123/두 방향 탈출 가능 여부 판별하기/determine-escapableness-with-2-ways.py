import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False for _ in range(m+1)] for _ in range(n+1)]

board = [
    [0 for _ in range(m+1)],
    *[[0, *list(map(int, input().split()))] for _ in range(n)]
    ]

def is_available(a, b):
    if a > n or b > n:
        return False
    if board[a][b] == 0:
        return False
    if visited[a][b] == True:
        return False
    return True

def dfs(a, b):
    dxys = [[1, 0], [0, 1]]
    for dx, dy in dxys:
        x, y = a + dx, b + dy
        if is_available(x, y):
            visited[x][y] = True
            dfs(x, y)

dfs(1, 1)

if visited[-1][-1]:
    print(1)
else:
    print(0)