n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_val = 0
for i in range(1, n+1):
    sum_val = 0
    for _ in range(m):
        sum_val += arr[i]
        i = arr[i]
    max_val = max(max_val, sum_val)
print(max_val)