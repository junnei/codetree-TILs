import sys

input = sys.stdin.readline

n = int(input())

for i in range(n-1):
    print("  "*(n-i-1)+"@ "*(i+1))

for i in range(n, 0, -1):
    print("@ "*i)