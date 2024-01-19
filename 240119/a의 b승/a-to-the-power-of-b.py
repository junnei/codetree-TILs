import sys

input = sys.stdin.readline

a, b = tuple(map(int,input().split()))
prod = 1

for i in range(1,b+1):
    prod *= a
print(prod)