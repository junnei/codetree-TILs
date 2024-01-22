import sys

input = sys.stdin.readline

string = input().rstrip()
n = int(input())

print(string[-1:-min(len(string),n)-1:-1])