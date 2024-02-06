n, t = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(3)
]

t %= n*2
for i in range(t):
    arr = [[arr[(i-1)%3][-1]] + arr[i][:-1] for i in range(3)]

for i in arr:
    print(*i)