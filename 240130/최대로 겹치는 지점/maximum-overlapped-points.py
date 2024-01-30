n = int(input())

datas = [map(int, input().split()) for _ in range(n)]

result = [0] * (100+1)

for x1, x2 in datas:
    for i in range(x1, x2+1):
        result[i] += 1

print(max(result))