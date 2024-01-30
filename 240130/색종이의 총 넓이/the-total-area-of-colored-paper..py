OFFSET = 100
result = [[0 for _ in range(2*OFFSET+1)] for _ in range(2*OFFSET+1)]

n = int(input())
datas = [map(int, input().split()) for _ in range(n)]

for x1, y1 in datas:
    x1, y1 = x1+OFFSET, y1+OFFSET
    for x in range(x1, min(x1 + 8, 200)):
        for y in range(y1, min(y1 + 8, 200)):
            result[x][y] = 1

print(sum([sum(i) for i in result]))