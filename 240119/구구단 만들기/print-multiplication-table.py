import sys

input = sys.stdin.readline

a, b = map(int,input().split())

if b%2 != 0:
    b -= 1

for i in range(1, 10): 
    for j in range(b, a-1, -2):
        print(f"{j} * {i} = {i * j}", end="")
        if j != a and j != a+1:
            print(" / ", end="")
    print()