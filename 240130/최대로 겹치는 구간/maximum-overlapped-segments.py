n = int(input())

datas = [map(lambda x: int(x) + 100, input().split()) for _ in range(n)]

result = [0] * (200+1)

for x1, x2 in datas:
    for i in range(x1, x2):
        result[i] += 1

print(max(result))