import sys

input = sys.stdin.readline

arr = input().rstrip().split()

for string in arr[::-1]:
    print(string)