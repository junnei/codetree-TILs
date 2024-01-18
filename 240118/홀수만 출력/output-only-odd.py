import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

if a%2 == 0:
    a += 1
for num in range(a, b+1, 2):
    print(num, end=" ")