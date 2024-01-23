import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] for _ in range(n+1)]
is_visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

def dfs(x, board):
    if is_visited[x] == 1:
        return
    is_visited[x] = 1
    for i in board[x][1:]:
        dfs(i, board)

dfs(1, board)

print(sum(is_visited[2:]))