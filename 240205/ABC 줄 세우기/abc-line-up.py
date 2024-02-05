n = int(input())

arr = list(map(lambda x: ord(x)-65, input().split()))

cnt = 0
for i in range(n):
    if arr[i] == i:
        continue
    else:
        found = arr.index(i)
        arr[i:found+1] = [arr[found]]+arr[i:found]
        cnt += found - i
print(cnt)