import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
is_visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

def dfs(x):
    for i in board[x]:
        if not is_visited[i]:
            is_visited[i] = True
            dfs(i)

dfs(1)

print(sum(is_visited[2:]))