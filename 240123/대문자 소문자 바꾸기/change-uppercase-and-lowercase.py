import sys

input = sys.stdin.readline

string = input().rstrip()

for char in string:
    if char >= 'a' and char <= 'z':
        print(char.upper(), end="")
    elif char >= 'A' and char <= 'Z':
        print(char.lower(), end="")