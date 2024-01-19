import sys

input = sys.stdin.readline

n = int(input())
num = 10
for i in range(1, n+1):
    for j in range(1, n+1):
        num -= 1
        if num==0:
            num = 9
        print(num, end="")
    print()