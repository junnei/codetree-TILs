import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

if a<90 or b<90:
    print(0)
elif b>=95:
    print(100000)
else:
    print(50000)