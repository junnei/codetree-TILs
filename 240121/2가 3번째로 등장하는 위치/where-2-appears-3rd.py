import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for idx, num in enumerate(arr):
    if num == 2:
        cnt+=1
        if cnt >= 3:
            cnt = idx
            break
print(cnt+1)