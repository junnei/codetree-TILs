import sys

input = sys.stdin.readline

a, n = tuple(map(int, input().split()))


for i in range(1,n+1):
    print(a+n*i)