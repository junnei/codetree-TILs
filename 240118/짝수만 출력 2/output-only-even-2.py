import sys

input = sys.stdin.readline

b, a = tuple(map(int, input().split()))

while a <= b:
    print(b, end=" ")
    b-=2