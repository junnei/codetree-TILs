import sys

input = sys.stdin.readline

n = int(input())

if n>=80:
    print("pass")
else:
    print(f"{80-n} more score")