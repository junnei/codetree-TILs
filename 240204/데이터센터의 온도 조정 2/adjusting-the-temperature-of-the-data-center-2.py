N, C, G, H = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

MAX_TEMP = 1000
max_work = 0
for i in range(MAX_TEMP + 1):
    work = 0        
    for ta, tb in arr:
        if i < ta:
            work += C
        elif ta <= i <= tb:
            work += G
        else:
            work += H
    max_work = max(max_work, work)
print(max_work)