import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

print(arr.count(m))