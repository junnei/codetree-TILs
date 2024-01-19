import sys

input = sys.stdin.readline

n = int(input())

cnt = 0

for i in range(n, 0, -1): 
    print("  "*(n-i), end="")
    for j in range(i, 0, -1):
        cnt += 1
        if cnt == 10:
            cnt = 1
        print(cnt, end=" ")
    print()