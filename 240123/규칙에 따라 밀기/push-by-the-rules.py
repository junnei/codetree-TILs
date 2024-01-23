import sys

input = sys.stdin.readline

s = input().rstrip()
commands = input().rstrip()

for command in commands:
    if command == 'L':
        s = s[1:] + s[0]
    elif command == 'R':
        s = s[-1] + s[:-1]
print(s)