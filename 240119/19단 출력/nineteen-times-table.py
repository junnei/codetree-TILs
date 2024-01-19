import sys

input = sys.stdin.readline

n = 19

for i in range(1, n+1): 
    for j in range(1, n+1):
        print(f"{i} * {j} = {i*j}", end="")
        if j%2 == 0:
            print()
        elif j != 19:
            print(" / ", end="")
        else:
            print()