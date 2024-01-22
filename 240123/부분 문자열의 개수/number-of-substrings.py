import sys

input = sys.stdin.readline

string = input().rstrip()
sub = input().rstrip()
cnt = 0

for i in range(len(string)-1):
    if sub[0] == string[i] and sub[1] == string[i+1]:
            cnt += 1
print(cnt)