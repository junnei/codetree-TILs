import sys

input = sys.stdin.readline

a = input().rstrip()

num = ord(a)-1 if a > 'a' else ord('z')
print(chr(num))