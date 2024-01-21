import sys

input = sys.stdin.readline

arr = ['L', 'E', 'B', 'R', 'O', 'S']

c = input().rstrip()

if c in arr:
    print(arr.index(c))
else:
    print("None")