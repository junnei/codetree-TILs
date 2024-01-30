n = int(input())

datas = [input().split() for _ in range(n)]

result = [0] * (2000+1)
idx = 1000
for val, command in datas:
    if command == "L":
        for i in range(idx-int(val), idx):
            result[i] += 1
        idx-=int(val)
    else:
        for i in range(idx, idx+int(val)):
            result[i] += 1
        idx+=int(val)

sum_val = 0
for i in result:
    if i >= 2:
        sum_val += 1
print(sum_val)