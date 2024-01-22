import sys

input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
len_str = 0
cnt = 0

for string in arr:
    len_str += len(string)
    if string[0] == 'a':
        cnt += 1
print(len_str, cnt)