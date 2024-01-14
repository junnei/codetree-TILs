n, m = list(map(int, input().split()))
vertex = [list(map(int, input().split())) for _ in range(m)]

matrix = [[0] * n for _ in range(n)]

visited = [0] * n

for x, y in vertex:
    matrix[x-1][y-1] = 1

def getAvailable(x):
    result = []
    for idx, isAvailable in enumerate(matrix[x]):
        if isAvailable == 1:
            if visited[idx] == 0:
                result.append(idx)
    return(result)

def explore(x):
    if visited[x] == 0:
        visited[x] = 1
        for point in getAvailable(x):
            explore(point)

explore(1 - 1)
print(sum(visited[1:]))