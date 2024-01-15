import sys

input = sys.stdin.readline

a_math, a_eng = tuple(map(int, input().split()))
b_math, b_eng = tuple(map(int, input().split()))

if a_math > b_math:
    print("A")
elif b_math > a_math:
    print("B")
elif a_eng > b_eng:
    print("A")
else:
    print("B")