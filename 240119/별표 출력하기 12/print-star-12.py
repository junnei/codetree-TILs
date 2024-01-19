import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    for j in range(n):
        if i > j or (j%2 == 0 and i!= 0):
            print("  ", end="")
        else:
            print("* ", end="")
    print()