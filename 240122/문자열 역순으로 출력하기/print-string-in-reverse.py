import sys

input = sys.stdin.readline

string = [input().rstrip() for _ in range(4)]

for i in string[::-1]:
    print(i)