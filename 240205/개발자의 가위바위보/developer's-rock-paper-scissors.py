n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for a, b in arr:
    result[a-1][b-1] += 1

max_cnt = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i == j or j==k or k == i:
                continue
            cnt = result[i][j] + result[j][k] + result[k][i]
            max_cnt = max(max_cnt, cnt)
print(max_cnt)