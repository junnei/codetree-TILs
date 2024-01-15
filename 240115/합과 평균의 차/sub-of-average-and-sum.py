import sys

input = sys.stdin.readline

a, b, c = list(map(int, input().split()))

print(a+b+c)
print(int((a+b+c)/3))
print(a+b+c-int((a+b+c)/3))