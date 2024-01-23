import sys

input = sys.stdin.readline

arr = input().rstrip().split()

result = 0

for string in arr:
    found = False
    for i in range(len(string)):
        if not string[i].isdigit():
            result += int(string[:i])
            found = True
            break
    if found == False:
        result += int(string[:i])
print(result)