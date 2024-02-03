n = int(input())
arr = list(map(int, input().split()))

min_diff = 10200
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        diff = 0
        temp = arr[:j]+arr[j+1:]
        for k in range(1, n-1):
            diff += abs(temp[k] - temp[k-1])
        min_diff = min(diff, min_diff)
    arr[i] //= 2
print(min_diff)