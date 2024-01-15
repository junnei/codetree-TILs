import sys

input = sys.stdin.readline

a = int(input())

if a % 13 == 0 or a % 19 == 0:
    print(True)
else:
    print(False)