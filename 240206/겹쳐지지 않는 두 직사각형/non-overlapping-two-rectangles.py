n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_val = -25000

for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1 + 1, n+1):
            for y2 in range(y1 + 1, m+1):
                for a1 in range(n):
                    for b1 in range(m):
                        for a2 in range(a1 + 1, n+1):
                            for b2 in range(b1 + 1, m+1):
                                if x2 <= a1 or a2 <= x1 or b2 <= y1 or y2 <= b1:
                                    sum_val = 0
                                    for i in range(x1, x2):
                                        sum_val += sum(arr[i][y1:y2])
                                    for i in range(a1, a2):
                                        sum_val += sum(arr[i][b1:b2])
                                    max_val = max(max_val, sum_val)
print(max_val)