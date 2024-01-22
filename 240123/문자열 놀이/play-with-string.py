import sys

input = sys.stdin.readline

s, q = input().rstrip().split()
queries = [input().rstrip().split() for _ in range(int(q))]

for query in queries:
    if query[0] == '1':
        a, b = s[int(query[1]) - 1], s[int(query[2]) - 1]
        s = s[:int(query[1]) - 1] + b + s[int(query[1]):]
        s = s[:int(query[2]) - 1] + a + s[int(query[2]):]
        print(s)
    elif query[0] == '2':
        s = s.replace(query[1], query[2])
        print(s)