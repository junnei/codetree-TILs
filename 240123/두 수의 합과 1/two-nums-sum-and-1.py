import sys

input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

string = str(a+b)
cnt = 0

for char in string:
    if char == '1':
        cnt += 1
print(cnt)