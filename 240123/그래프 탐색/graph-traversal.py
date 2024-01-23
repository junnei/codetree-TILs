import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
is_visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
cnt = 0
def dfs(x):
    global cnt
    for i in board[x]:
        if not is_visited[i]:
            is_visited[i] = True
            cnt += 1
            dfs(i)
            
is_visited[1] = True
dfs(1)
print(cnt)