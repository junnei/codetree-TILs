import sys

input = sys.stdin.readline

a = int(input())

if a % 4 == 0 and a % 100 != 0:
    print('true')
elif a % 400 == 0:
    print('true')
else:
    print('false')