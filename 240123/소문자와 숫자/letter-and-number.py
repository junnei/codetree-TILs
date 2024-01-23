import sys

input = sys.stdin.readline

string = input().rstrip()

for char in string:
    if char.isalpha() or char.isdigit():
        print(char.lower(), end="")