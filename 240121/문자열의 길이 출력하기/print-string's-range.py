import sys

input = sys.stdin.readline

arr = [input().rstrip() for _ in range(2)]

print(sum([len(s) for s in arr]))