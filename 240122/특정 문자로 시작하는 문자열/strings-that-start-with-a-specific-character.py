import sys

input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for i in range(n)]
c = input().rstrip()

cnt = 0
len_str = 0

for string in arr:
    if string[0] == c:
        cnt += 1
        len_str += len(string)

print(cnt, f"{len_str/cnt:.2f}")