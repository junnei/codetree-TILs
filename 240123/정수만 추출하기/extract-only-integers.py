import sys

input = sys.stdin.readline

arr = input().rstrip().split()

result = 0

for string in arr:
    for i in range(len(string)):
        if not string[i].isdigit():
            result += int(string[:i])
            break
print(result)