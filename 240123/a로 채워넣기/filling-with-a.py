import sys

input = sys.stdin.readline

string = input().rstrip()
string = list(string)
string[1] = 'a'
string[-2] = 'a'
print(''.join(string))