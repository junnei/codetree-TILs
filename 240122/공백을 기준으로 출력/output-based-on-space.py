import sys

input = sys.stdin.readline

string = [input().rstrip().split() for _ in range(2)]

print(''.join([''.join(string[i]) for i in range(2)]))