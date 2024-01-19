import sys

input = sys.stdin.readline

n = int(input())

for i in range(n*2-1):
    print("* "*(i+1 if i<n else n*2-1-i))