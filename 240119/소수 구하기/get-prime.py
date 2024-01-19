import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    for j in range(2, i+1):
        if i % j == 0:
            print(i, end=" ")
            break