n = int(input())

datas = [input().split() for _ in range(n)]
idx = 100000
result = [0 for _ in range(2*idx+1)]

for val, command in datas:
    if command == "L":
        for i in range(int(val)):
            result[idx-i] = 1
        idx-=int(val)-1
    else:
        for i in range(int(val)):
            result[idx+i] = 2
        idx+=int(val)-1

sum_val = [0, 0, 0]
for data in result:
    if data != 0:
        sum_val[data] += 1
print(*sum_val[1:])