n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

max_cnt = 0
for k in range(1, 1001):
    cnt = 0
    group = arr[0] > k
    for i in range(n):
        if group:
            if arr[i] <= k:
                group = False
                cnt += 1
        else:
            if arr[i] > k:
                group = True
    if group:
        cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)