n, b = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = 0

for i in range(n):
    temp = arr[:]
    temp[i][0] //= 2
    temp.sort(lambda x : x[0]+x[1])

    sum_val = 0
    cnt = 0
    for j in range(n):
        sum_val += temp[j][0] + temp[j][1]
        if sum_val > b:
            break
        cnt += 1
    max_val = max(max_val, cnt)
print(max_val)