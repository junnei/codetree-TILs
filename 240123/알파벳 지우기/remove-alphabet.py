import sys

input = sys.stdin.readline

arr = [input().rstrip() for _ in range(2)]

result = 0

for string in arr:
    num = ""
    for char in string:
        if char.isdigit():
            num += char
    result += int(num)
print(result)