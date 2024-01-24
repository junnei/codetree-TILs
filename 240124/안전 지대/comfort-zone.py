import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [[0] * (m+1)] + [[0] + list(map(int, input().rstrip().split())) for _ in range(n)]

visited = [[False for _ in range(m+1)] for _ in range(n+1)]

def is_range(a, b):
    if (1<=a and a<=n) and (1<=b and b<=m):
        return True
    else:
        return False

def is_available(a, b, k):
    if not is_range(a, b):
        return False
    if board[a][b] <= k:
        return False
    if visited[a][b] == True:
        return False
    return True

def dfs(a, b, k):
    dxys = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in dxys:
        x, y = a + dx, b + dy
        if is_available(x, y, k):
            visited[x][y] = True
            dfs(x, y, k)

result = [0] * 100

for k in range(1, 100+1):
    cnt = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if is_available(i, j, k):
                visited[i][j] = True
                cnt += 1
                dfs(i, j, k)
    result[k - 1] = cnt
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]

max_areas = max(result)

print(result.index(max_areas) + 1, max_areas)