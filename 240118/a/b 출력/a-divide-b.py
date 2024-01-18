import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

print(a//b, end=".")

for i in range(20):
    a *= 10
    print(a//b, end="")
    a %= b