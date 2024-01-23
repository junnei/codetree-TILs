import sys

input = sys.stdin.readline

string = input().rstrip()

for i in range(len(string), -1, -1):
    print(string[i:] + string[:i])