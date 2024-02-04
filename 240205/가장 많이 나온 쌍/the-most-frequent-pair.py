n, m = map(int, input().split())
arr = [
    set(map(int, input().split()))
    for _ in range(m)
]

max_val = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        count = 0
        for item in arr:
            if set([i, j]) == item:
                count += 1
        max_val = max(max_val, count)
print(max_val)