n = int(input())

OFFSET = 100

datas = [map(int, input().split()) for _ in range(n)]
result = [[0 for _ in range(2*OFFSET+1)] for _ in range(2*OFFSET+1)]

for x1, y1, x2, y2 in datas:
    for x in range(x1, x2):
        for y in range(y1, y2):
            result[x][y] = 1

print(sum([sum(i) for i in result]))