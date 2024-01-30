OFFSET = 1000
result = [[0 for _ in range(2*OFFSET+1)] for _ in range(2*OFFSET+1)]

datas = [map(int, input().split()) for _ in range(2)]

for idx, (x1, y1, x2, y2) in enumerate(datas):
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            result[x][y] = 1 - idx

min_x, min_y, max_x, max_y = 2000, 2000, 0, 0
if sum([sum(row) for row in result]) == 0:
    print(0)
else:
    for i, row in enumerate(result):
        for j, val in enumerate(row):
            if val == 1:
                if i < min_x:
                    min_x = i
                if i > max_x:
                    max_x = i
                if j < min_y:
                    min_y = j
                if j > max_y:
                    max_y = j

    print((max_x-min_x+1)*(max_y-min_y+1))