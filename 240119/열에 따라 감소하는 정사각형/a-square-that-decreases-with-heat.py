import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()