import sys

input = sys.stdin.readline

string = input().rstrip()
sub = input().rstrip()

print(string.find(sub))