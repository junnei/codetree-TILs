import sys

input = sys.stdin.readline

n = int(input())

for i in range(2, n+1):
    found = False
    for j in range(2, i):
        if i % j == 0:
            found = True
            break
    if found != True:
        print(i, end=" ")