import sys

input = sys.stdin.readline

string = input().rstrip()

index = string.index('e')
print(string[:index]+string[index+1:])