n = int(input())
arr = list(map(int, input().split()))

cnt = 0
last_num = 101
for i in range(n-1, -1, -1):
    if arr[i] < last_num:
        last_num = arr[i]
        cnt += 1
    else:
        break
print(n-cnt)