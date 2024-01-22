import sys

input = sys.stdin.readline

string = input().rstrip()
mem = [string[0], 1]
result = ""

for char in string[1:]:
    if mem[0] == char:
        mem[1] += 1
    else:
        result += mem[0] + str(mem[-1])
        mem = [char, 1]

result += mem[0] + str(mem[-1])
print(len(result))
print(result)