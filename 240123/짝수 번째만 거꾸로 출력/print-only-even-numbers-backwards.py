import sys

input = sys.stdin.readline

string = input().rstrip()

for char in string[-1::-2]:
    print(char, end="")