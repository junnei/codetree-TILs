n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_cnt = 0
for i in range(1, 4):
    cnt = 0
    temp = [False] * 4
    temp[i] = True

    for a, b, c in arr:
        temp[a], temp[b] = temp[b], temp[a]
        if temp[c]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)