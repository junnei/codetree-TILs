n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            found = True
            line = [False] * 100
            for idx in range(n):
                if idx == i or idx == j or idx == k:
                    continue
                a, b = arr[idx]
                if True in line[a-1:b+1-1]:
                    found = False
                    break
                line[a-1:b+1-1] = [True] * (b-a+1)
            if found:
                cnt += 1
print(cnt)