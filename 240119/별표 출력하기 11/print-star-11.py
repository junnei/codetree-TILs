import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, 2*n+2):
    if i%2 != 0:
        print("* "*((2*n)+1))
    else:
        print("*   "*(n+1))