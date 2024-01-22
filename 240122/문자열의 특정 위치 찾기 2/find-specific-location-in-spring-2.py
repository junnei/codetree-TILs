import sys

input = sys.stdin.readline

data = ["apple", "banana", "grape", "blueberry", "orange"]
c = input().rstrip()
cnt = 0

for i in data:
    if c in i[2:4]:
        print(i)
        cnt += 1
print(cnt)