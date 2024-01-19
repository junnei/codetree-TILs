import sys

input = sys.stdin.readline

n, m = tuple(map(int,input().split()))

for _ in range(n):
    print("* "*m)