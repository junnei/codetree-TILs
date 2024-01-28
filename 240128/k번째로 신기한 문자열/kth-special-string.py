n, k, T = map(lambda x: int(x) if x[0] >= '0' and x[0] <='9' else x,input().split())

arr = [input() for _ in range(n)]
arr.sort()

cnt = 0
for i in range(n):
    if arr[i].startswith(T):
        cnt = i
        break

print(arr[cnt+k-1])