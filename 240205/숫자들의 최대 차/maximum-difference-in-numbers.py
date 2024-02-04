n, k = map(int, input().split())

arr = [0] * 10001
for _ in range(n):
    arr[int(input())] += 1
max_val = 0
for i in range(1, 10001):
    max_val = max(max_val, sum(arr[i:i+k+1]))
print(max_val)