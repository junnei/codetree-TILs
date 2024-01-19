import sys

input = sys.stdin.readline

n = int(input())

for i in range(n*2-1):
    print("* "*(n-i if i<n else i+2-n))