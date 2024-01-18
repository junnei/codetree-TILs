import sys

input = sys.stdin.readline

n = int(input())
cnt= [0] * 3

for i in range(1,n+1):
    if i%12 == 0:
        cnt[2] += 1
    elif i%3 == 0:
        cnt[1] += 1
    elif i%2 == 0:
        cnt[0] += 1
print(*cnt)