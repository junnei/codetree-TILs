import sys

input = sys.stdin.readline

m = int(input())
lines = [int(input()) for _ in range(m)]

for n in lines:
    cnt = 0
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1

    print(cnt)