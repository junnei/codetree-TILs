import sys

input = sys.stdin.readline

a, b = tuple(map(int,input().split()))
found = False

for i in range(a,b+1):
    if 1920 % i == 0 or 2880 % i == 0:
        found = True
print(1 if found else 0)