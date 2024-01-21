import sys

input = sys.stdin.readline

a, b = map(int, input().split())
arr = [0]*10

while a>1:
    arr[a%b] += 1
    a = a//b

result = 0
for cnt in arr:
    result += cnt*cnt
print(result)