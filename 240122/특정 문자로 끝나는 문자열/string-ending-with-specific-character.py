import sys

input = sys.stdin.readline

arr = [input().rstrip() for i in range(10)]
c = input().rstrip()
cnt = 0
for string in arr:
    if string[-1] == c:
        print(string)
        cnt += 1
if cnt == 0:
    print("None")