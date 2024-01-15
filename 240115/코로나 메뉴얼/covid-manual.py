import sys

input = sys.stdin.readline

people = [input().rstrip().split() for _ in range(3)]

answer = 0

for cond, temp in people:
    if cond == "Y" and int(temp) >= 37:
        answer += 1
print("E" if answer >= 2 else "N")