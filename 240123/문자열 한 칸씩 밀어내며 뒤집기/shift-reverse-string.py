import sys

input = sys.stdin.readline

s, q = input().rstrip().split()
queries = [int(input()) for _ in range(int(q))]

for query in queries:
    if query == 1:
        s = s[1:] + s[0]
    elif query == 2:
        s = s[-1] + s[:-1]
    else:
        s = s[::-1]
    print(s)