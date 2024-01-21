import sys

input = sys.stdin.readline

arr = [input().rstrip().split() for i in range(3)]
cnt = [0]*4

for a, b in arr:
    if int(b)>=37:
        if a=="Y":
            cnt[0] += 1
        else:
            cnt[1] += 1
    else:
        if a=="Y":
            cnt[2] += 1
        else:
            cnt[3] += 1
print(*cnt, end=" ")
if cnt[0] >= 2:
    print("E")