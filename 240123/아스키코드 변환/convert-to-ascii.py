import sys

input = sys.stdin.readline

a, b = input().rstrip().split()

print(ord(a), chr(int(b)))