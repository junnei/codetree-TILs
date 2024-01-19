import sys

input = sys.stdin.readline

m = int(input())
lines = [int(input()) for _ in range(m)]
cnt = 0

for n in lines:
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

print(cnt)