import sys

input = sys.stdin.readline

arr = input().rstrip().split()

print(arr[0][:2]+arr[1][2:])