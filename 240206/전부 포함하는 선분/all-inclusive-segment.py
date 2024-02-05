n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_diff = 100
for i in range(n):
    start = 100
    end = 0
    for a, b in arr[:i]+arr[i+1:]:
        start = min(start, a)
        end = max(end, b)
    min_diff = min(min_diff, end - start)
print(min_diff)