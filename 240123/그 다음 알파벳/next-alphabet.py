import sys

input = sys.stdin.readline

a = input().rstrip()

num = ord(a)+1 if ord('z') >= ord(a) + 1 else ord('a')
print(chr(num))