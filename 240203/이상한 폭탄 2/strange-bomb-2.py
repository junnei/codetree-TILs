n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_num = -1
for i in range(n):
    if arr[i] in arr[i+1:min(i+k+1, n)]:
        max_num = max(max_num, arr[i])
print(max_num)