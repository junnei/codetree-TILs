import sys

input = sys.stdin.readline

n = int(input())

if n>= 3000:
    print("book")
elif n>= 1000:
    print("mask")
else:
    print("no")