import sys

input = sys.stdin.readline

a, b = [input().rstrip() for _ in range(2)]
cnt = -1

for i in range(1, len(a) + 1):
    if b == a[i:] + a[:i]:
        cnt = i
        break
print(cnt)