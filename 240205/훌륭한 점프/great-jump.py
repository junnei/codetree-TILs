n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_NUM = 100

answer = 0

for i in range(1, MAX_NUM+1):
    if arr[0] > i or arr[-1] > i:
        continue

    cnt = 0
    possible = True
    for num in arr:
        if num <= i:
            cnt = 0
            continue
        cnt += 1
        if cnt >= k:
            possible = False
            break
    if possible:
        print(i)
        break