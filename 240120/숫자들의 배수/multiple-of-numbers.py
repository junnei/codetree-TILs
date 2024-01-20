import sys

input = sys.stdin.readline

n = int(input())
arr = []
cnt = 0
cnt_five = 0

while cnt_five<2:
    cnt += 1
    arr.append(n*cnt)
    if n*cnt % 5 == 0:
        cnt_five += 1

print(*arr)