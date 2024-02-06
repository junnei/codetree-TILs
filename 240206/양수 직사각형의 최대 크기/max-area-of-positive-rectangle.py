n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_size = -1

for x1 in range(n):
    for x2 in range(x1+1, n+1):
        for y1 in range(n):
            for y2 in range(y1+1, m+1):
                if all(all([num > 0 for num in arr[i][y1:y2]]) for i in range(x1, x2)):
                    max_size = max(max_size, (x2-x1)*(y2-y1))
print(max_size)