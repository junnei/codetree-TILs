import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

if a%2 == 1:
    a+=1
while a <= b:
    print(a, end=" ")
    a+=2