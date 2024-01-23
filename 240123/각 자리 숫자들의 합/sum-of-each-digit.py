import sys

input = sys.stdin.readline

string = input().rstrip()
result = 0

for char in string:
    result += int(char)
print(result)