k, n = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(k)
]

found = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for data in arr:
    for i in range(n):
        for j in range(i+1, n):
            found[data[i]-1][data[j]-1] += 1

answer = 0
for i in range(n):
    for j in range(n):
        if found[i][j] >= 1 and found[j][i] == 0:
            answer += 1
print(answer)