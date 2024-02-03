T, a, b = map(int, input().split())
arr = [
    input().split()
    for _ in range(T)
]
cnt = 0
for k in range(a, b+1):
    d1 = 1000
    d2 = 1000
    for char, x in arr:
        if char == "S":
            d1 = min(d1, abs(int(x)-k))
        else:
            d2 = min(d2, abs(int(x)-k))
    if d1 <= d2:
        cnt += 1
print(cnt)