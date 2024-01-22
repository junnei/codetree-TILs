import sys

input = sys.stdin.readline

n = int(input())
string = [input().rstrip() for _ in range(n)]

print(''.join(string))