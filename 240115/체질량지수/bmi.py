import sys

input = sys.stdin.readline

a, b = tuple(map(int, input().split()))

rate = int((b*10000) / (a**2))
print(rate)

if rate>=25:
    print("Obesity")