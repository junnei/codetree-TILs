import sys
sys.setrecursionlimit(2500)

input = sys.stdin.readline

n = int(input())
matrix = [
    list(map(int, input().rstrip().split()))
    for _ in range(n)
    ]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
    ]

def is_range(a, b):
    return (0 <= a and a < n) and (0 <= b and b < n)

def is_available(a, b, k):
    if not is_range(a, b):
        return False
    if visited[a][b] or matrix[a][b] != k:
        return False
    return True

def dfs(a, b, k):
    global cnt
    dxys = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in dxys:
        x, y = a + dx, b + dy
        if is_available(x, y, k):
            visited[x][y] = True
            cnt += 1
            dfs(x, y, k)

min_k = min(list(map(min, matrix)))
max_k = max(list(map(max, matrix)))

answer_num = 0
max_block_size = 0

for k in range(min_k, max_k + 1):
    nearby = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            if is_available(i, j, k):
                visited[i][j] = True
                cnt += 1
                dfs(i, j, k)
                nearby.append(cnt)
                
    for block_size in nearby:
        if block_size >= 4:
            answer_num += 1
        if block_size > max_block_size:
            max_block_size = block_size
    visited = [[False for _ in range(n)] for _ in range(n)]
    
print(answer_num, max_block_size)