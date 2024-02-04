n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_NUM = 100

answer = 0

for i in range(1, MAX_NUM+1):
    cnt = 0
    if arr[0] > i:
        continue
    
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