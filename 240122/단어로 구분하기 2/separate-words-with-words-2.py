import sys

input = sys.stdin.readline

arr = input().rstrip().split()

for idx, string in enumerate(arr):
    if idx % 2 == 0:
        print(string)