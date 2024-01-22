import sys

input = sys.stdin.readline

n = int(input())
arr = input().rstrip().split()
string = ''.join(arr)

i = 0
while i + 5 <= len(string):
    print(string[i:i+5])
    i += 5
print(string[i:])