import sys

input = sys.stdin.readline

string = input().rstrip()
result = 0

for char in string:
    if char.isdigit():
        result += int(char)
print(result)