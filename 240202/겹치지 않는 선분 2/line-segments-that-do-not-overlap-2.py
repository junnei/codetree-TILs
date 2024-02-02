n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
for i in range(n):
    found = False
    for j in range(n):
        if i==j:
            continue
        if not found and (points[i][0] < points[j][0]) ^ (points[i][1] < points[j][1]):
            found = True
    if not found:
        cnt += 1
        
print(cnt)