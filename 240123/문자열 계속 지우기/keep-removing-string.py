import sys

input = sys.stdin.readline

a, b = [input().rstrip() for _ in range(2)]

index = a.find(b)
while index != -1:
    a = a[:index] + a[index + len(b):]
    index = a.find(b)
print(a)