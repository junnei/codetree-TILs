n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

from itertools import combinations

cnt = 0
dxs = [0, 1, 2, 3]
dys = [3, 2, 1, 0]
for dx, dy in zip(dxs, dys):
    for x in list(combinations(range(11), dx)):
        for y in list(combinations(range(11), dy)):
            found = True
            for i, j in arr:
                if not (i in x or j in y):
                    found = False
                    break
            if found:
                cnt+=1
                break
        if found: break
if cnt:
    print(1)
else:
    print(0)