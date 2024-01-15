import sys

input = sys.stdin.readline

C = input().rstrip()

if C=='S':
    print("Superior")
elif C=='A':
    print("Excellent")
elif C=='B':
    print("Good")
elif C=='C':
    print("Usually")
elif C=='D':
    print("Effort")
else:
    print("Failure")