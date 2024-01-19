import sys

input = sys.stdin.readline

n = int(input())

for i in range(2*n-1):
    print("  "*(i if i<n else 2*n-1-i-1)+"* "*(2*n-1-2*i if i<n else 2*i-2*n+3))