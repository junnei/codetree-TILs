import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if cnt == 8:
            cnt = 0
        cnt += 2
        print(cnt, end=" ")
    print()