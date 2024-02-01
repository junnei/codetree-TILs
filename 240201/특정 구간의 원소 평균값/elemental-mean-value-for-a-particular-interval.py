n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i, n):
        avg_val = sum(arr[i:j+1]) / (j-i+1)
        if avg_val in arr[i:j+1]:
            cnt += 1
print(cnt)