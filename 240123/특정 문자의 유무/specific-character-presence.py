import sys

input = sys.stdin.readline

string = input().rstrip()

a = "Yes" if 'ee' in string else "No"
b = "Yes" if 'ab' in string else "No"

print(a, b)