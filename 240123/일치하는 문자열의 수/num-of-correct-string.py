import sys

input = sys.stdin.readline

n, a = input().rstrip().split()
arr = [input().rstrip() for _ in range(int(n))]
cnt = 0

for string in arr:
    if string == a:
        cnt += 1
print(cnt)