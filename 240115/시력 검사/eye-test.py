import sys

input = sys.stdin.readline

a, b = [float(input().rstrip()) for _ in range(2)]

if a >= 1.0 and b >= 1.0:
    print("High")
elif a >= 0.5 and b>= 0.5:
    print("Middle")
else:
    print("Low")