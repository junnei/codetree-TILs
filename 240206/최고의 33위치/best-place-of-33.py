n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = 0
for i in range(n-2):
    for j in range(n-2):
        sum_val = 0
        for k in range(3):
            sum_val += sum(arr[i+k][j:j+3])
        max_val = max(max_val, sum_val)
print(max_val)