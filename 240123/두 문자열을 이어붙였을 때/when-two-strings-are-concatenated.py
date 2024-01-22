import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

print('true' if str1+str2 == str2+str1 else 'false')