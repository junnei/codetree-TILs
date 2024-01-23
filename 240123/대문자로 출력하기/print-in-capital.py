import sys

input = sys.stdin.readline

string = input().rstrip()

for char in string:
    if char.isalpha():
        print(char.upper(), end="")