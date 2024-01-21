import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [0]*10

for num in arr:
    result[num] += 1

for i in result[1:]:
    print(i)