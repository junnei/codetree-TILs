import sys

input = sys.stdin.readline

string = input().rstrip()
cnt = [0, 0]
for i in range(len(string)-1):
    if string[i] == 'e':
        if string[i+1] == 'e':
            cnt[0] += 1
        elif string[i+1] == 'b':
            cnt[1] += 1

print(*cnt)