import sys

input = sys.stdin.readline

n = int(input())

print("vapor" if n >= 100 else "water" if n>=0 else "ice")