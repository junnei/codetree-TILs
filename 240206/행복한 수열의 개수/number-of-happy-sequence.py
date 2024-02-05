n, m = map(int, input().split())
arr = [
    input().split()
    for _ in range(n)
]

cnt = 0
for i in range(n):
    line = ''.join(arr[i])
    for j in range(n-m+1):
        sub = ''.join([arr[i][j]] * m)
        if sub in line:
            cnt += 1
            break
    
    row = ''.join([j[i] for j in arr])
    
    for j in range(n-m+1):
        sub = ''.join([arr[j][i]] * m)
        if sub in row:
            cnt += 1
            break
print(cnt)