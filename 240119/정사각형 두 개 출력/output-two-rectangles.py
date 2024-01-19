import sys

input = sys.stdin.readline

n = int(input())

for _ in range(2):
    for _ in range(n):
        print("*"*n)
    print()