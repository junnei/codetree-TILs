import sys

input = sys.stdin.readline

n = int(input())
found = False

for i in range(2, n):
    if n % i ==0:
        found = True
        break
print("C" if found else "P")