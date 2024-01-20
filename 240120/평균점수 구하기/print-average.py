import sys

input = sys.stdin.readline

arr = list(map(float, input().split()))

avg = round(sum(arr)/len(arr), 1)
print(avg)