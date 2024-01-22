import sys

input = sys.stdin.readline

string = input().rstrip()
sub = input().rstrip()
cnt = 0

for i in range(len(string)):
    if string[i:].find(sub) == 0:
        cnt += 1
print(cnt)