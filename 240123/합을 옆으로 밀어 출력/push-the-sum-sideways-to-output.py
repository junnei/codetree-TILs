import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

string = str(sum(arr))

print(string[1:]+string[0])