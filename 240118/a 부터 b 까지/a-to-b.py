import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

limit = a

for i in range(a, b+1):
    if i == limit:
        print(i, end=" ")
        if i % 2 == 1:
            limit *= 2
        else:
            limit += 3