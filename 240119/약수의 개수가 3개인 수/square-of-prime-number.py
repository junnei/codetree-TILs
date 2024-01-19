import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))
cnt = 0

for i in range(a, b+1):
    result = 0
    for j in range(1, i+1):
        if i % j == 0:
            result += 1
    if result == 3:
        cnt += 1
print(cnt)