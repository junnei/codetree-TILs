OFFSET = 100
result = [[0 for _ in range(2*OFFSET+1)] for _ in range(2*OFFSET+1)]

n = int(input())
datas = [map(int, input().split()) for _ in range(n)]

for idx, (x1, y1, x2, y2) in enumerate(datas):
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            result[x][y] = idx % 2

print(sum([sum(row) for row in result]))