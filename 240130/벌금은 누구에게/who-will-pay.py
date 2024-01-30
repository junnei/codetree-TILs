datas = []

n, m, k = map(int, input().split())

for _ in range(m):
    datas.append(int(input()))


result = [0 for _ in range(n+1)]

answer = -1
for i in datas:
    result[i] += 1
    if result[i] >= k:
        answer = i
        break
print(answer)