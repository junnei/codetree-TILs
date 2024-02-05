n = int(input())
arr = list(map(int, list(input())))

dist = []
cnt = 1
max_cnt = 0
max_idx = 0
for i in range(1, n):
    if arr[i] == 1:
        if cnt > max_cnt:
            max_cnt = cnt
            max_idx = len(dist)
        dist.append(cnt)
        cnt = 1
    else:
        cnt += 1
val = dist.pop(max_idx)
dist.extend([val-val//2, val//2])
print(min(dist))