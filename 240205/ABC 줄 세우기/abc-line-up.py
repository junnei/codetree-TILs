n = int(input())

arr = list(map(lambda x: ord(x)-65, input().split()))

cnt = 0
for i in range(n):
    if arr[i] == i:
        continue
    else:
        found = arr.index(i)
        arr[i], arr[found] = arr[found], arr[i]
        cnt += 1
print(cnt)