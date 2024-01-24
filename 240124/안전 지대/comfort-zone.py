import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [
    list(map(int, input().rstrip().split())) for _ in range(n)
    ]

visited = [[False for _ in range(m)] for _ in range(n)]

def is_range(a, b):
    return (0 <= a and a < n) and (0 <= b and b < m)

def is_available(a, b, k):
    if not is_range(a, b):
        return False
    if visited[a][b] or board[a][b] <= k:
        return False
    return True

def dfs(a, b, k):
    dxys = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in dxys:
        x, y = a + dx, b + dy
        if is_available(x, y, k):
            visited[x][y] = True
            dfs(x, y, k)

min_k = max(min(list(map(min, board))) - 1, 1)
max_k = max(list(map(max, board)))

max_cnt = -1
answer_k = 0

for k in range(min_k, max_k + 1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if is_available(i, j, k):
                visited[i][j] = True
                cnt += 1
                dfs(i, j, k)
    if cnt > max_cnt:
        answer_k, max_cnt = k, cnt

    for i in range(n):
        for j in range(m):
            visited[i][j] = False
    
print(answer_k, max_cnt)