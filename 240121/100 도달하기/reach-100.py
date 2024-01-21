import sys

input = sys.stdin.readline

n = int(input())
a = 1

print(1, n, end=" ")

while n<=100:
    a, n = n, a+n
    print(n, end =" ")