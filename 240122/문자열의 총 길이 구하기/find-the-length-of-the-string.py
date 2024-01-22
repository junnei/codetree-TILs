import sys

input = sys.stdin.readline

string = input().rstrip().split()
cnt = 0
for i in string:
    cnt += len(i)
print(cnt)