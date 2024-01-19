import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    for _ in range(n-i):
        print("*"*(n-i),end=" ")
    print()