n, k = map(int, input().split())
arr = [
    int(input())
    for _ in range(n)
]

max_val = 0
max_int = 0



for i in range(n):
    num = arr[i]
    d = 1
    j = 1
    cnt = 0
    while d <= k:
        if i+j >= n:
            break
        if arr[i+j] == num:
            cnt += 1
            d = 0
        else:
            d += 1
        j += 1
    
    if cnt > max_val:
        max_val = cnt
        max_int = num

if max_val == 0:
    print(0)
else:
    print(max_int)