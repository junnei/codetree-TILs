import sys

input = sys.stdin.readline

while True:
    a, b, c = input().rstrip().split()
    print(int(a)*int(b))
    if c == "C":
        break