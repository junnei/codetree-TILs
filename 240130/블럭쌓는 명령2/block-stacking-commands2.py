n, k = map(int, input().split())

datas = [map(int, input().split()) for _ in range(k)]

result = [0] * (n+1)

for a, b in datas:
    for i in range(a, b+1):
        result[i] += 1

print(max(result))