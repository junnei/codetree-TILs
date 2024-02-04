N, L = map(int, input().split())
arr = list(map(int, input().split()))

MAX_H = 100
for i in range(MAX_H + 1):
    cnt = 0
    upper = 0
    for num in arr:
        if num >= i:
            cnt += 1
        elif num == i - 1:
            upper += 1
    if cnt + min(L, upper) < i:
        print(i-1)
        break