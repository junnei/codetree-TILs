n = int(input())

datas = [input().split() for _ in range(n)]

result = [[0, 0, 0] for _ in range(200000+1)]
idx = 100000
for val, command in datas:
    if command == "L":
        for i in range(idx-int(val), idx):
            result[i][0] += 1
            result[i][2] = 0
        idx-=int(val)
    else:
        for i in range(idx, idx+int(val)):
            result[i][1] += 1
            result[i][2] = 1
        idx+=int(val)
        
sum_val = [0, 0, 0]
for x, y, color in result:
    if x >= 2 and y >= 2:
        sum_val[2] += 1
    elif x >= 1 or y >= 1:
        sum_val[color] += 1
print(*sum_val)