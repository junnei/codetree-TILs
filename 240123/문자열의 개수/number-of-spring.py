import sys

input = sys.stdin.readline

cnt = 0
arr = []

while True:
    s = input().rstrip()
    if s == '0':
        break
    cnt += 1
    if cnt % 2 == 1:
        arr.append(s)

print(cnt)
for value in arr:
    print(value)