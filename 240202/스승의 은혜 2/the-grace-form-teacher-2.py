n, b = map(int, input().split())
prices = [
    int(input())
    for _ in range(n)
]

max_cnt = 0
for i in range(n):
    arr = prices[:]
    arr[i] = arr[i]//2
    arr.sort()

    cnt = 0
    sum_val = 0
    for item in arr:
        sum_val += item
        if sum_val > b:
            break
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)