import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(5)]
found = False

for i in nums:
    if i % 3 != 0:
        found = True
print(0 if found else 1)