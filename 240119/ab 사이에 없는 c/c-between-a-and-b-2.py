import sys

input = sys.stdin.readline

a, b, c = tuple(map(int,input().split()))
found = False

for i in range(a,b+1):
    if i % c == 0:
        found = True
print("NO" if found else "YES")